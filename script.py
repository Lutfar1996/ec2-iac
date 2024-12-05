import boto3
import requests
import time

# Constants
AWS_REGION = 'us-east-1'  # Update with your region
EC2_INSTANCE_ID = 'i-0dec7ae1549dba4a1'  # Replace with your EC2 instance ID
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1313802165546127431/uCAPg__UqCS1cv8tpMbol1FHQnSBYDu3lBkOmaQo3puNgToE9uOVeVNDL3_NII-hn4fo'  # Replace with your Discord webhook URL

# Initialize AWS EC2 client
ec2_client = boto3.client('ec2', region_name=AWS_REGION)

def check_ec2_status():
    """
    Checks the status of the EC2 instance.
    Returns the status of the EC2 instance.
    """
    response = ec2_client.describe_instances(InstanceIds=[EC2_INSTANCE_ID])
    instance = response['Reservations'][0]['Instances'][0]
    return instance['State']['Name']

def send_discord_message(message):
    """
    Sends a message to Discord using a webhook URL.
    """
    data = {
        'content': message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent to Discord successfully!")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

def main():
    print("Monitoring EC2 instance status...")
    while True:
        instance_status = check_ec2_status()
        if instance_status == 'stopped':
            message = f"Warning! Your EC2 instance ({EC2_INSTANCE_ID}) has stopped."
            send_discord_message(message)
            print(f"Message sent: {message}")
            break  # Stop the loop after sending the message
        time.sleep(60)  # Check the status every minute

if __name__ == "__main__":
    main()
