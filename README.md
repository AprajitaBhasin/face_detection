# Face-Detection Software
A utility to detect faces in a picture using Microsoft Azure Face PaaS Service. 

## Pre-requisites
- Python Library
- Microsoft Azure Subscription

## Setup Environment
- Using the Azure subcription, create a Face resource
- Copy the key and endpoint details from the face resource and export the details into following environment variables respectively:
FACE_SUBSCRIPTION_KEY and FACE_ENDPOINT.

## Execution

```sh
$ cd face_detection
$ python face.py
```

Sample output

![N|Solid](https://docs.microsoft.com/en-us/azure/cognitive-services/Face/images/face-rectangle-result.png)

