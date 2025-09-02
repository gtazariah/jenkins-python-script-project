pipeline {
    agent any
    
    environment {
        REPO_URL = 'https://github.com/gtazariah/jenkins-python-script-project'
        EMAIL_RECIPIENT = 'azariah.gt@gmail.com'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main', 
                    url: 'https://github.com/gtazariah/jenkins-python-script-project.git',
                    credentialsId: 'github-credentials'
            }
        }
        
        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        
        stage('Run Script') {
            steps {
                echo 'Running Python script...'
                sh 'python3 simple_script.py'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running basic tests...'
                sh 'python3 -c "import sys; exec(open(\'simple_script.py\').read()); sys.exit(0)"'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed. Sending email notification...'
            script {
                def buildStatus = currentBuild.currentResult
                emailext (
                    subject: "Jenkins Build ${buildStatus}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                    Build: ${env.JOB_NAME} #${env.BUILD_NUMBER}
                    Status: ${buildStatus}
                    URL: ${env.BUILD_URL}
                    
                    Console Output: ${env.BUILD_URL}console
                    
                    GitHub Repository: ${env.REPO_URL}
                    """,
                    to: "${env.EMAIL_RECIPIENT}",
                    attachLog: true
                )
            }
        }
        
        success {
            echo 'Pipeline succeeded!'
        }
        
        failure {
            echo 'Pipeline failed!'
        }
        
        unstable {
            echo 'Pipeline unstable!'
        }
    }
}
