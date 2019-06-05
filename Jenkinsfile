pipeline {
    agent {
        docker { image 'python:3.7.2' }
    }
    stage('Build') {
        echo 'building...'
        sh 'python --version'
    }
    stage('Test') {
        echo 'testing...'
        sh 'python test/test.py'
    }
    stage('Ship') {
        echo 'shipping...'
    }
}