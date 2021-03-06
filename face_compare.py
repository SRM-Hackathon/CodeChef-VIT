import csv
import boto3
import subprocess as sp
#import S3add_trust as S3tr

with open('AWScreds.csv','r') as input:
    next(input)
    reader= csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
source_photo= './images/tar.jpg'
#target_photo= './images/tar.jpg'
client= boto3.client('rekognition',
                    aws_access_key_id= access_key_id ,
                        aws_secret_access_key=secret_access_key, region_name='ap-south-1')
with open(source_photo, 'rb') as source_image:
    source_bytes = source_image.read()
#with open(target_photo, 'rb') as source_image:
#    target_bytes = source_image.read()
f= open("trusted.txt","r")
if f.mode== "r":
    contents = f.read()
    response = client.compare_faces(SimilarityThreshold=90,SourceImage={
            'Bytes': source_bytes},
            TargetImage={
            'S3Object': {
                    'Bucket': 'trusted-members',
                    'Name': 'dipto.jpg'
                    }
                }
                    )
# Use Attributes parameter for details other than default values
#print(response)
#print(type(response))
#print(response['Labels'][0]['Confidence'])
    '''for key,value in response.items():
        if key in ('FaceMatches','UnmatchedFaces'):
            print(key)
            for att in value:
                print(att)'''
   # x=key.get("Similarity")
    #print(x)
    '''for key,value in response.items():
        if key in ('FaceMatches'):
            string_key = dict([(str(k),v) for k,v in key.items()])
            print(string_key)'''
    if(len(response['FaceMatches'])>0):
        for facematch in response['FaceMatches']:
            conf= str(facematch['Face']['Confidence'])
            print("Confidence level is ",conf)
            sp.getoutput("ansible-playbook --vault-password-file='/CodeChef-VIT/.secret'  msg.yml")
    else:
        print("Unknown Person")
        sp.getoutput("python S3add_strangers.py")