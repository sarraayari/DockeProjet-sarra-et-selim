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

                    sh 'docker build -t svm-service:latest .'

                    // Run the Docker container
                    sh 'docker run  -p 5002:5002 svm-service'
                }
            }
        }

      
        
}
}
