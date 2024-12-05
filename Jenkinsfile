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
                      // Ensure python3-venv is installed
                     sh 'sudo apt update && sudo apt install -y python3.12-venv'

                     // Create the virtual environment
                     sh 'python3 -m venv venv'

                    // Activate the virtual environment and install requirements
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
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
