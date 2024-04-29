pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-app_streamlit")
                }
            }
        }
        stage('Push Docker Image to Registry') {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com/', 'credentials-id') {
                        docker.image("my-app_streamlit").push("latest")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    kubectl.apply(file: 'deployment.yml')
                    kubectl.apply(file: 'service.yml')
                }
            }
        }
    }
}
