# record-audio
Record a audio and upload it to `AWS S3` bucket using `flask`. File will be uploaded to S3 bucket inside `input` folder.

## Getting started
### Clone repository

```shell
$ git clone https://github.com/kartikkaklotar/record-audio.git
```

### Set up a virtualenv

```shell
$ cd record-audio
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Install dependencies

```shell
$ pip install -r requirements.txt
```

### Update values in the main.py file
```python3
10. session = boto3.Session(profile_name='PROFILE_NAME') # Update name of the AWS profile
14. bucket_name = 'BUCKET_NAME' # Update name of the bucket
```

### Run the server

```shell
$ flask --app main run [--debug]
```

Open localserver to test the feature

[Home](http://localhost:5000/)
