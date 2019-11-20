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
                    junit 'test/test-reports/*.xml'
                }
            } 
        }
        stage('Code Analysis') {
            steps {
                script {
                    echo 'code analysis...'
                    sh 'pylint src/*.py'
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