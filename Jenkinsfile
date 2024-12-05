pipeline {
    agent any  // Run the pipeline on any available Jenkins agent
    
    environment {
        // GITHUB_TOKEN = credentials('github-token')
        // Set environment variables for AWS credentials
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')  // Jenkins credential for AWS Access Key
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')  // Jenkins credential for AWS Secret Key
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the public repository containing your Python script
               git branch: 'main', url: 'https://github.com/Lutfar1996/ec2-iac.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'sudo apt-get update'
                    
                    sh 'sudo apt install python3-pip -y'  // Install pip if not already installed
                    sh 'pip install -r requirements.txt'  // Install dependencies
                   
                }
            }
        }

        stage('Run EC2 Monitor Script') {
            steps {
                script {
                    // Run the Python script to monitor the EC2 instance and send a message to Discord
                    sh 'python3 script.py'  // Adjust the command based on the location of your Python script
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
