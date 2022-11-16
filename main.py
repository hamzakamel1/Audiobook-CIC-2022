## Name: Hamza Kamel Ahmed
## ID: 20190659

import os
from google.cloud import texttospeech_v1
import PyPDF2
from tkinter.filedialog import *

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= 'audiobook-projectcic-f36a013c7af0.json'
client = texttospeech_v1.TextToSpeechClient()

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = pdfreader.numPages

for num in range (0,pages):
    page = pdfreader.getPage(num)
    text= page.extractText()
print(text)

synthesis_input = texttospeech_v1.SynthesisInput(text=text)


voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

voice2 = texttospeech_v1.VoiceSelectionParams(
    name= 'en-US-Wavenet-J',
    language_code="en-US"
)

print(client.list_voices)
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
    request={"input": synthesis_input, "voice": voice1, "audio_config": audio_config}
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

