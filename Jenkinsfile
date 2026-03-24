pipeline{
    agent {label 'vinod'}
    stages{
        stage("clone"){
            steps{
                echo "cloning the code ..."
                sh "sleep 4s"
                git branch: "main" , url: "https://github.com/nitin-panwar-6963/image-uploader.git"
                echo "cloneing successfully.."
            }
        }
        stage("build"){
            steps{
                echo "build your docker image .."
                sh "sleep 4s"
                sh "docker build -t image-app ."
                echo "your image build successfully..."
            }
        }
        stage("deploy"){
            steps{
                echo "deploying you code..."
                sh "docker run -p 8000:8000 -e AWS_ACCESS_KEY_ID= -e AWS_SECRET_ACCESS_KEY= -e AWS_REGION= -e AWS_S3_BUCKET_NAME= -e DYNAMODB_TABLE_NAME= image-app"
            }
        }
    }
}
