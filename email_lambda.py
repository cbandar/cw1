import json
import boto3

def send_email(event_body):
    ses = boto3.client('ses')
    sender_email = "test@test.com"
    recipient_email = "cosmin.alecs@icloud.com"
message_content = str(event_body) + 'does not contain any PPE!'

try:
	ses.send_email(
		Source=sender_email,
		Destination={
			'ToAddresses':[recipient_email]
		},
		Message={
		Subject:{
			'Data':'test'
		},
		'Body':{
			'Text':{
				'Data': event_body
				}
			}
		},
		ReplyToAddresses=[sender_email]



def lambda_handler(event, context):
  s3 = boto3.resource('s3')
  table = boto3.resource('dynamodb').Table('S2027892_Audio_Data')

  # Check the DynamoDB table is populated with all image data
  if len(table.scan()['Items']) == len(s3.Bucket('s2027892').objects.all()):
    print('All audio files have been uploaded to S3!')

    results = []
    for item in table.scan()['Items']:
      results.append(str(item['file_Name']))

    event_body = event['Records'][0]['body']
    if event_body not in results:

      send_sms(event_body)
      print('Email sent!' + '\n' + str(event_body) + ' test' + '\n')
    else:
          print(str(event_body) + ' test2' + '\n')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
