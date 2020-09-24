
# importing required python libraries
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

# Let the FACE_SUBSCRIPTION_KEY environment variable equal the key value from your Face service instance.
FACE_KEY = os.environ['FACE_SUBSCRIPTION_KEY']

# Let the FACE_ENDPOINT environment variable equal the endpoint value from your Face service instance.
FACE_ENDPOINT = os.environ['FACE_ENDPOINT']

# Using the Endpoint and Key values, create an authenticated FaceClient.
face_client = FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(FACE_KEY))

# Detect a face in an image that contains a single face
# Replace url with your image url
SINGLE_FACE = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
single_image_name = os.path.basename(SINGLE_FACE)
detected_faces = face_client.face.detect_with_url(url=SINGLE_FACE)
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Display the detected face ID in the first single-face image.
print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()

# Save this ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id


# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    
    return ((left, top), (right, bottom))


# Download the image from the url
response = requests.get(SINGLE_FACE)
img = Image.open(BytesIO(response.content))

# For each face returned use the face rectangle and draw a red box.
print('Drawing rectangle around face... see popup for results.')
draw = ImageDraw.Draw(img)
# Count no. of people in image
count = 0
for face in detected_faces:
    draw.rectangle(getRectangle(face), outline='red')
    count += 1

# Display the image in the users default image browser.
img.show()
# identify no. of people
print(" The number of people identified are: " + count)


