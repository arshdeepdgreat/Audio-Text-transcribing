import speech_recognition as sr
from os import path
from pydub import AudioSegment

# transcribe audio file                                                         
AUDIO_FILE = input("enter audio file name: ")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  
        print("Transcription: " + r.recognize_google(audio))