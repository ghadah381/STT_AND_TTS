from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '8kbLd5nBuUPTp3jF3LdVoq29fmC0YmQWfVfdIqSsX0wF'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/cc2a13af-5a9c-4038-aa17-1415d5f05b67'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

with open('churchill.txt', 'r') as f:
    text = f.readlines()

text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)

with open('./wanston.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)