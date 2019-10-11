# How to run the image recognition model
import csv
import boto3
from datetime import datetime

with open('AWS creds.csv','r') as input:
    next(input)
    reader= csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
# datetime object containing current date and time
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# Indexing each staranger with current date and  time which must be unique
photo= './images/tar.jpg'
faces.append(dt_string)
s3= boto3.client('s3',
                    aws_access_key_id= access_key_id ,
                        aws_secret_access_key=secret_access_key, region_name='ap-south-1')
s3.upload_file('./images/bus.jpg','stranger-members','{}.jpg').format(dt_string)
