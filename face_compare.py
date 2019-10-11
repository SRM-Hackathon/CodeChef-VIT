import csv
import boto3

with open('AWS creds.csv','r') as input:
    next(input)
    reader= csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
source_photo= './images/src.jpg'
target_photo= './images/tar.jpg'
client= boto3.client('rekognition',
                    aws_access_key_id= access_key_id ,
                        aws_secret_access_key=secret_access_key, region_name='ap-south-1')
with open(source_photo, 'rb') as source_image:
    source_bytes = source_image.read()
with open(target_photo, 'rb') as source_image:
    target_bytes = source_image.read()
