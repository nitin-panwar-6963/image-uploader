# 📸 Django Image Upload App (S3 + DynamoDB + Docker)

A modern **full-stack Django application** with:

* 🔐 User Authentication (Login/Register)
* ☁️ Image Upload to AWS S3
* 🗄️ User Data stored in DynamoDB
* 🎨 Modern Dark UI (HTML + CSS)
* 🐳 Fully Dockerized

---

## 🚀 Features

* ✅ Register & Login system (DynamoDB)
* ✅ Upload images to AWS S3
* ✅ Secure password hashing
* ✅ Session-based authentication
* ✅ Modern dark UI design
* ✅ Docker support

---

## 🧱 Tech Stack

* Backend: Django
* Frontend: HTML, CSS
* Cloud: AWS S3 + DynamoDB
* Container: Docker
* SDK: boto3

---

## 📁 Project Structure

```
image_upload_app/
│── config/
│── app/
│── templates/
│── static/
│── Dockerfile
│── requirements.txt
│── .env
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone https://github.com/your-username/image-upload-app.git
cd image-upload-app
```

---

### 2️⃣ Create `.env` file

```
SECRET_KEY=your_secret_key
DEBUG=True

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1

AWS_S3_BUCKET_NAME=your-bucket-name
DYNAMODB_TABLE_NAME=users-table
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Locally

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🐳 Run with Docker

### Build Image

```bash
docker build -t image-app .
```

### Run Container

```bash
docker run -d -p 8000:8000 --env-file .env --name myapp image-app
```

---

## ☁️ AWS Setup

### 🔹 S3 Bucket

* Create a bucket
* Disable "Block Public Access" (for public images)

---

### 🔹 S3 Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

---

### 🔹 IAM Policy (Attach to User)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3UploadAccess",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

---

### 🔹 DynamoDB Table

* Table Name: `users-table`
* Partition Key: `username (String)`

---

### 🔹 DynamoDB Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:GetItem"
      ],
      "Resource": "arn:aws:dynamodb:ap-south-1:*:table/users-table"
    }
  ]
}
```

---

## 🔐 Security Notes

* ❌ Do NOT commit `.env` file
* ❌ Do NOT expose AWS keys publicly
* ✅ Use IAM roles in production
* ✅ Use pre-signed URLs for private access

---

## ⚠️ Common Issues

### ❌ `AccessControlListNotSupported`

👉 Remove `ACL: public-read` from code

---

### ❌ `django_session` error

```bash
python manage.py migrate
```

---

### ❌ CSRF error

Ensure:

```
{% csrf_token %}
```

---

## 🎯 Future Improvements

* 📸 Image gallery (multiple uploads)
* ❤️ Like / Delete functionality
* 🔐 JWT Authentication
* ⚛️ React frontend
* ☁️ Deploy on AWS EC2

---

## 👨‍💻 Author

* Nitin Panwar

---

## ⭐ Support

If you like this project:

👉 Star the repo
👉 Share with others

---

## 📜 License

This project is licensed under the MIT License.
