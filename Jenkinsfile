pipeline {
    agent any

    stages {

        stage('Install deps') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Create .env') {
            steps {
                writeFile file: '.env', text: '''
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
BROWSER_VERSION=128.0
'''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Publish Allure') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
