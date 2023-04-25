# cw1 
# student number s2027892

import boto3

def create_ec2_instance(instance_type, key_name):
  #init ec2
  ec2 = boto3.resource('ec2')
  instances = ec2.create_instances(
    ImageId='ami-02396cdd13e9a1257',
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type,
    KeyName=key_name,
    IamInstanceProfile={ 
      'Arn' : 'arn:aws:iam::785522309505:instance-profile/LabInstanceProfile'
    }
  )

  #validate ec2
  if instances:
    print('ec2 % s created' % instances[0].id)
  return

def create_sns_topic(topic_name):
  #init sns
  sns = boto3.resource('sns')
  topic = sns.create_topic(Name=topic_name)

  #validate sns
  if topic:
    print('SNS Topic % s created' % topic_name)
  return

def create_bucket(bucket_name, region_name):
  #init s3 bucket
  session = boto3.Session(region_name=region_name)
  s3_client = session.client('s3')
  s3_client.create_bucket(Bucket=bucket_name)
  
  #validate s3 bucket
  buckets_list = s3_client.list_buckets()
  for bucket in buckets_list['Buckets']:
    if bucket['Name'] == 'bucket-s2027892':
      print('bucket created')
      break
    else:
      print('bucket not created')
      break
  return

create_ec2_instance('t2.micro', '2027892')
create_sns_topic('sns-s2027892')
create_bucket('bucket-s2027892', 'us-east-1')
