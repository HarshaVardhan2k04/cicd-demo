pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'python -m flake8 --select=E9,F63,F7,F82 app.py test_app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest test_app.py -v'
            }
        }
    }
}
