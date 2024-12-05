pipeline {
    agent any

    environment {
        // AWS Credentials ID from Jenkins credentials store
        AWS_CREDENTIALS_ID = 'aws-credentials' // Replace with your AWS credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Lutfar1996/ec2-iac.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install necessary dependencies, create virtual environment
                    sh '''#!/bin/bash
                        sudo apt update && sudo apt install -y python3.12-venv
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Use withCredentials to inject AWS IAM credentials
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        credentialsId: AWS_CREDENTIALS_ID // AWS credentials ID
                    ]]) {
                        // Run your python script with AWS credentials available
                        sh '''#!/bin/bash
                            source venv/bin/activate
                            python3 script.py
                        '''
                    }
                }
            }
        }
    }
}
