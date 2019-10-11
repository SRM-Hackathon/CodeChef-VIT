# How to run the image recognition model
import csv
import boto3

with open('AWS creds.csv','r') as input:
    next(input)
    reader= csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
#photo= './images/hapwo.jpg'
name=input("Enter the user name")
photo= './images/{}.jpg'.format(name)
faces.append(name)
s3= boto3.client('s3',
                    aws_access_key_id= access_key_id ,
                        aws_secret_access_key=secret_access_key, region_name='ap-south-1')
s3.upload_file('./images/bus.jpg','imagehack','bus.jpg')
