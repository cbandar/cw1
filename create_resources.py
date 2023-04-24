import boto3

# Create EC2 Instance
def create_ec2_instance(instance_type, key_name):
  ec2 = boto3.resource('ec2')
  instances = ec2.create_instances(
    ImageId='ami-02396cdd13e9a1257',
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type,
    KeyName=key_name,
  )

#EC2 Instance
  if instances:
    print('EC2 Instance % s created' % instances[0].id)
  return

# Create SNS Topic
def create_sns_topic(topic_name):
  sns = boto3.resource('sns')
  topic = sns.create_topic(Name=topic_name)

  if topic:
    print('SNS Topic % s created' % topic_name)
  return

  #  Create S3 Bucket
def create_bucket(bucket_name, region_name):
  session = boto3.Session(region_name=region_name)
  s3_client = session.client('s3')
  s3_client.create_bucket(Bucket=bucket_name)

  # Validate S3 Bucket
  buckets_list = s3_client.list_buckets()
  for bucket in buckets_list['Buckets']:
    if bucket['Name'] == 'bucket-s2027892':
      print('S3 Bucket created')
      break
    else:
      print('S3 Bucket not created')
      break
  return

create_ec2_instance('t2.micro', 'vockey1')
create_sns_topic('sns-s2027892')
create_bucket('bucket-s2027892', 'us-east-1')
