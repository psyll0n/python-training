# Cloud Services

Cloud platform integrations and services. This section covers working with cloud providers, particularly Amazon Web Services (AWS).

## 📂 Contents

### [AWS](./aws/)
Amazon Web Services integration examples using boto3 SDK.

#### Simple Queue Service (SQS)
Message queuing service for distributed applications.

**send_sqs_message.py** - Sending messages to SQS queue
- Message creation and formatting
- Queue URL configuration
- Error handling with boto3
- Message attributes
- Batch sending support

**receive_sqs_messages.py** - Receiving and processing messages
- Long polling for efficiency
- Message visibility timeout
- Message deletion after processing
- Error handling
- Batch message retrieval

**SQS Basics:**
```python
import boto3

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

# Send message
response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue',
    MessageBody='Hello from Python!'
)

# Receive messages
messages = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20  # Long polling
)

# Process and delete
for message in messages.get('Messages', []):
    # Process message
    print(message['Body'])
    
    # Delete message
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
```

**SQS Use Cases:**
- Decoupling microservices
- Asynchronous processing
- Load leveling
- Buffering requests
- Message broadcasting (with SNS)
- Order processing
- Background job queues

**Key Concepts:**
- **Queue URL** - Unique identifier for queue
- **Message Body** - Actual message content (up to 256 KB)
- **Receipt Handle** - Token for message deletion
- **Visibility Timeout** - Time message is hidden after retrieval
- **Dead Letter Queue** - Failed message handling
- **Long Polling** - Efficient message retrieval

---

## ☁️ AWS Services Overview

### Compute
- **EC2** - Virtual servers
- **Lambda** - Serverless functions
- **ECS/EKS** - Container orchestration
- **Elastic Beanstalk** - PaaS for web apps

### Storage
- **S3** - Object storage
- **EBS** - Block storage for EC2
- **EFS** - File storage
- **Glacier** - Archive storage

### Database
- **RDS** - Relational databases
- **DynamoDB** - NoSQL database
- **ElastiCache** - In-memory cache
- **Aurora** - MySQL/PostgreSQL compatible

### Messaging
- **SQS** - Message queue (shown in this section)
- **SNS** - Publish/subscribe notifications
- **EventBridge** - Event bus
- **Kinesis** - Real-time data streaming

### Security
- **IAM** - Identity and access management
- **Secrets Manager** - Secret storage
- **KMS** - Encryption key management
- **Cognito** - User authentication

---

## 🔧 Setting Up AWS with Python

### Install boto3
```bash
pip install boto3
```

### Configure Credentials

**Method 1: AWS CLI**
```bash
aws configure
# Enter: Access Key, Secret Key, Region, Output format
```

**Method 2: Credentials File**
```
# ~/.aws/credentials
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

# ~/.aws/config
[default]
region = us-east-1
output = json
```

**Method 3: Environment Variables**
```bash
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
export AWS_DEFAULT_REGION=us-east-1
```

**Method 4: In Code (NOT recommended for production)**
```python
import boto3

client = boto3.client(
    'sqs',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-east-1'
)
```

---

## 💡 Best Practices

### Security
```python
import os
import boto3

# Use environment variables
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Or use IAM roles (best for EC2/Lambda)
# No credentials needed - boto3 auto-detects
client = boto3.client('sqs')
```

### Error Handling
```python
import boto3
from botocore.exceptions import ClientError

try:
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'QueueDoesNotExist':
        print("Queue not found")
    elif error_code == 'AccessDenied':
        print("Permission denied")
    else:
        print(f"Error: {e}")
```

### Resource Management
```python
# Use context managers when available
with open('data.txt') as f:
    data = f.read()

# Clean up resources
try:
    # Use resource
    pass
finally:
    # Cleanup
    client.close()
```

### Logging
```python
import logging

# Enable boto3 logging
boto3.set_stream_logger('boto3.resources', logging.INFO)

# Your own logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info('Sending message to SQS')
```

---

## 🎯 Common Patterns

### SQS Producer-Consumer
```python
# Producer (send_sqs_message.py pattern)
def send_to_queue(queue_url, message):
    """Send message to SQS queue"""
    sqs = boto3.client('sqs')
    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message
        )
        return response['MessageId']
    except ClientError as e:
        logger.error(f"Error sending message: {e}")
        raise

# Consumer (receive_sqs_messages.py pattern)
def process_queue(queue_url):
    """Process messages from SQS queue"""
    sqs = boto3.client('sqs')
    
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20
        )
        
        for message in response.get('Messages', []):
            try:
                # Process message
                process_message(message['Body'])
                
                # Delete on success
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
            except Exception as e:
                logger.error(f"Error processing: {e}")
                # Message will become visible again
```

### Batch Operations
```python
# Send batch
entries = [
    {'Id': '1', 'MessageBody': 'Message 1'},
    {'Id': '2', 'MessageBody': 'Message 2'},
]
sqs.send_message_batch(QueueUrl=queue_url, Entries=entries)

# Receive batch
messages = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10
)

# Delete batch
entries = [
    {'Id': '1', 'ReceiptHandle': handle1},
    {'Id': '2', 'ReceiptHandle': handle2},
]
sqs.delete_message_batch(QueueUrl=queue_url, Entries=entries)
```

---

## 📊 SQS Queue Types

### Standard Queue
- **Ordering**: Best-effort, not guaranteed
- **Delivery**: At-least-once, may have duplicates
- **Throughput**: Nearly unlimited
- **Use Case**: High throughput, order not critical

### FIFO Queue
- **Ordering**: Guaranteed (First-In-First-Out)
- **Delivery**: Exactly-once
- **Throughput**: Up to 3,000 messages/sec
- **Use Case**: Order critical, no duplicates
- **Queue Name**: Must end with .fifo

---

## 🚀 Extending to Other AWS Services

### S3 (Storage)
```python
s3 = boto3.client('s3')

# Upload file
s3.upload_file('local.txt', 'my-bucket', 'remote.txt')

# Download file
s3.download_file('my-bucket', 'remote.txt', 'local.txt')

# List objects
response = s3.list_objects_v2(Bucket='my-bucket')
```

### Lambda (Serverless)
```python
lambda_client = boto3.client('lambda')

# Invoke function
response = lambda_client.invoke(
    FunctionName='my-function',
    InvocationType='RequestResponse',
    Payload=json.dumps({'key': 'value'})
)
```

### DynamoDB (NoSQL)
```python
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

# Put item
table.put_item(Item={'id': '123', 'name': 'John'})

# Get item
response = table.get_item(Key={'id': '123'})
```

---

## 📚 Resources

- **AWS Documentation**: docs.aws.amazon.com
- **Boto3 Docs**: boto3.amazonaws.com/v1/documentation
- **AWS Free Tier**: aws.amazon.com/free
- **AWS SDK Examples**: github.com/awsdocs/aws-doc-sdk-examples
- **AWS Architecture**: aws.amazon.com/architecture

## 💰 Cost Management

- Use AWS Free Tier for learning
- Set up billing alerts
- Use SQS standard queue (cheaper than FIFO)
- Delete unused resources
- Use auto-scaling appropriately
- Monitor with CloudWatch
