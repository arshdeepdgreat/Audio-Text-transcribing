import speech_recognition as sr
from os import path
from pydub import AudioSegment

# transcribe audio file                                                         
AUDIO_FILE = input("enter audio file name: ")
OUTPUT_FILE = input("enter output file name: ")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file   
        text=r.recognize_google(audio)
        f=open(OUTPUT_FILE,'w')
        f.write(text)
        f.close()
        print(text)