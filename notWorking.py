# Snippet from CloudFormation template
# Called after S3 Bucket sends a notification to SQS

import os
import json
from time import sleep
from botocore.exceptions import ClientError

transcriptDir = "transcriptions/"
ts = boto3.client("transcribe")
s3 = boto3.client("s3")
comp = boto3.client("comprehend")
db = boto3.client("dynamodb")

#transcribe file
def startTranscriptionJob(bucket, file, job):
	uri = getBucketUri(bucket, file)

	ts.start_transcription_job(
		TranscriptionJobName = job,
		Media = {
			"MediaFileUri": uri
		},
		MediaFormat = "mp3",
		LanguageCode = "en-GB",
		OutputBucketName = bucket,
		OutputKey = transcriptDir
	)

	states = ["COMPLETED", "FAILED", "CLIENT_ERROR"]
	while True:
		status = getTranscriptionStatus(job)
		if status in states:
			break
		sleep(5)
	return status

# Delete a transcribe job
def deleteTranscriptionJob(job):
	try:
		ts.delete_transcription_job(TranscriptionJobName = job)
		return False, ""
	except ClientError as error:
		print(error)
		return True, error
	except Exception as error:
		print(error)
		return True, error
