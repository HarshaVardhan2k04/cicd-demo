pipeline {
    agent any

    stages {
        stage('Setup venv & install') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'venv\\Scripts\\python.exe -m flake8 --select=E9,F63,F7,F82 app.py test_app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest test_app.py -v'
            }
        }
    }
}
