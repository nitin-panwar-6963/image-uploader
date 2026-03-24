from django.shortcuts import render, redirect
from .dynamodb import create_user, get_user, hash_password
from .s3_utils import upload_file
import uuid

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if get_user(username):
            return render(request, 'register.html', {'error': 'User already exists'})

        create_user(username, password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = get_user(username)

        if user and user['password'] == hash_password(password):
            request.session['user'] = username
            return redirect('dashboard')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def dashboard(request):
    if 'user' not in request.session:
        return redirect('login')

    image_url = None

    if request.method == "POST":
        image = request.FILES.get('image')

        if image:
            filename = str(uuid.uuid4()) + "_" + image.name
            image_url = upload_file(image, filename)

    return render(request, 'dashboard.html', {'image_url': image_url})


def logout_view(request):
    request.session.flush()
    return redirect('login')
