from flask import Flask, request
from flask import render_template
import boto3
import botocore
from uuid import uuid4

app = Flask(__name__)

# Set up AWS credentials
session = boto3.Session(profile_name='PROFILE_NAME') # Update name of the AWS profile
s3 = session.client('s3')

# Set up S3 bucket information
bucket_name = 'BUCKET_NAME' # Update name of the bucket

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    
    # Get file from request
    audio_file = request.files['audio']

    # Upload file to S3
    try:
        s3.upload_fileobj(audio_file, bucket_name, f'input/{uuid4()}.wav')
        return {'message':'File uploaded to S3!'}
    except botocore.exceptions.ClientError as e:
        print(e)
        return {'message':'Error uploading file to S3.'}

if __name__ == '__main__':
    app.run(debug=True)
