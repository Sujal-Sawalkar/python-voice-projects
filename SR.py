import sounddevice as sd
import speech_recognition as sr
import numpy as np
#variable created
recognizer = sr.Recognizer()

print("Speak something...")
duration = 5  
fs = 44100    
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

audio_data = sr.AudioData(recording.tobytes(), fs, 2)
try:
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand.")

