pipeline {
    agent any  // Run the pipeline on any available Jenkins agent
    
    environment {
        // Set environment variables, including GitHub credentials and AWS credentials
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')  // Jenkins credential for AWS Access Key
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')  // Jenkins credential for AWS Secret Key
        // GITHUB_CREDENTIALS = credentials('github-credentials')  // If using GitHub credentials (username/password or token)
    }

     stage('Checkout Code') {
            steps {
                // Clone the repository containing your Python script
                git url: 'https://github.com/your-username/your-repository.git', credentialsId: 'github-credentials'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install the required Python dependencies
                    sh 'pip install boto3 requests'
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
