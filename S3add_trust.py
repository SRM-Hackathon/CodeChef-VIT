import csv
import boto3
#import pandas as pd

trusted= "dip"
with open('AWScreds.csv','r') as input:
    next(input)
    reader= csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
# take user name to add
#name=input("Enter the user name")
faces=[]
photo= './images/tar.jpg'
# Taking photo directory
#name= "dipto"
faces.append(trusted)
print(trusted)
# Save Image with users name
#faces.append(name)
s3= boto3.client('s3',
                    aws_access_key_id= access_key_id ,
                        aws_secret_access_key=secret_access_key, region_name='ap-south-1')
s3.upload_file('./images/tar.jpg','trusted-members','{}.jpg'.format(trusted))
f= open('trusted.txt','a+')
f.write("{}\n".format(trusted))
f.close()