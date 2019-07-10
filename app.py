import requests
import json

import pandas as pd

subscription_key = '92d758df5cd64cc9a2339c33d21adebd'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

#image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

image_url = 'augment3/HAPPY/GW34-A-24.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

response = requests.post(face_api_url, params=params,
                                 headers=headers, json={"url": image_url})
j = json.dumps(response.json())
result = json.loads(j)

print(j)

emotions = ['anger', 'n', 'n', 'fear', 'happiness', 'neutral', 'sadness', 'n']


def change(emotion):
    current = ['anger', 'fear', 'happiness', 'neutral', 'sadness']
    transform = ['ANGRY', 'SCARED', 'HAPPY', 'NEUTRAL', 'SAD']
    result = ''
    for i in range(5):
        if current[i] == emotion:
            result = transform[i]
            break
    return result


anger = 0.000
fear = 0.000
happiness = 0.000
neutral = 0.000
sadness = 0.000
confidence = 0.000
emotion = ''

for emo in emotions:
    if emo == 'n':
        continue
    else:
        e = emo
        emo = result[0]['faceAttributes']['emotion'][emo]
        if emo > confidence:
            confidence = emo
            emotion = change(e)

print(emotion)
















