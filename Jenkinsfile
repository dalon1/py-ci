pipeline {
    agent {
        docker { image 'python:3.7.2' }
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo 'building...'
                    sh 'python --version'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'testing...'
                    sh 'python test/test.py'
                }
            } 
        }
        stage('Ship') {
            steps {
                script {
                    echo 'shipping...'
                }
            }
        }
    }
    
}