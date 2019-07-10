export = pd.read_excel('export.xlsx')
r = []

for f in range(len(export)):
    if export['type'].at[f] == 'TEST':
        image_url = export['name'].at[f][60:]
        label = export['label'].at[f]

        response = requests.post(face_api_url, params=params,
                                 headers=headers, json={"url": image_url})

        j = json.dumps(response.json())
        result = json.loads(j)

        emotions = ['anger', 'n', 'n', 'fear', 'happiness', 'neutral', 'sadness', 'n']

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

        r.__add__([emotion == label, confidence])

print(r)