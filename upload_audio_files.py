import os
import time
import boto3
import logging
from botocore.exceptions import ClientError

#logger config.
logger = logging.getLogger()
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s: %(levelname)s: %(message)s'
)

# upload to s3. 30 sec delay between uploads
def upload_audio_files(dir):
  session = boto3.Session()
  s3 = session.resource('s3')
  bucket = s3.Bucket('bucket-s2027892')
  for subdir, dirs, files in os.walk(dir):
    for file in files:
      dir_path = os.path.join(subdir, file)
      with open(dir_path, 'rb') as data:
        bucket.put_object(Key=dir_path[len(dir) + 1 :], Body=data)

        print('Uploaded ' + str(file))

        # Publish message to SNS.
        # message_id = ...
        message_id = publish_message(
          'arn:aws:sns:us-east-1:785522309505:sns-s2027892',
          file,
          'audio file  upload status'
        )
        print(message_id)
        time.sleep(30)

upload_audio_files('audio files')
