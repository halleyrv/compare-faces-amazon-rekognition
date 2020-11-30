import csv
import boto3
# settings.py
import settings
import os

NAME_PHOTO_TO_SEARCH = 'face_to_find.jpg'
NAME_PHOTO_TARGET_TO_COMPARE = 'photo_target_with_face.jpg'


class CompareFaces:
    
    def __init__(self):
        self.clientBoto3Amazon = self.__getClientToConnectWithAmazon()
    
    
    def __getClientToConnectWithAmazon(self):
        return boto3.client('rekognition',
                      aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
                      aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
                      region_name="us-east-2")            

    def detectIfFaceTargetExistWhenComparePhotos(self):
        photo_to_search_in_bytes = self.__getImageInBytesFormat(NAME_PHOTO_TO_SEARCH)
        target_photo_bytes = self.__getImageInBytesFormat(NAME_PHOTO_TARGET_TO_COMPARE)
        response = self.clientBoto3Amazon.compare_faces(
            SourceImage={'Bytes': photo_to_search_in_bytes},
            TargetImage={'Bytes': target_photo_bytes}
        )
        for key, value in response.items():
            if key in ('FaceMatches'):
                if (len(value) > 0):
                    print("Se detecto el rostro al comparar")
                    print("-----------------------")
                    for att in value:
                        print("Similitud:" + str(att['Similarity']) + "%")
                else:
                    print("No se encontro el rostro")          

    def __getImageInBytesFormat(self, nameImage):
        with open(nameImage, 'rb') as source_image:
            return source_image.read()  
         

obj = CompareFaces()
obj.detectIfFaceTargetExistWhenComparePhotos()

