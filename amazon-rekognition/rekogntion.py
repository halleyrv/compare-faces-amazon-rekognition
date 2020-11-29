import csv
import boto3

photo = 'face_to_find.jpg'
target_to_compare ='photo_target_without_face.jpg'

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]


client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name="us-east-2")

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()
    
with open(target_to_compare,'rb') as target_to_compare:
    target_photo_bytes = target_to_compare.read()

response = client.compare_faces(
    SourceImage={'Bytes': source_bytes},
    TargetImage={'Bytes': target_photo_bytes}
)

for key, value in response.items():
    if key in ('FaceMatches'):
        print("hee"+key)
        print(len(value))
        if (len(value)>0):
            print("Si existe foto")
        else:
            print("No")    
        #for att in value:
           # print(att)
#print(response)
