pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'  
    }

    stages { 
    
 stage('Build and Run Docker Image') {
            steps {
                script {
                    // Build and tag the Docker image

                    sh 'sudo docker build -t svm-service:latest .'

                    // Run the Docker container
                    sh 'sudo docker run  -p 5000:5000 svm-service'
                }
            }
        }

      
        
}
}
