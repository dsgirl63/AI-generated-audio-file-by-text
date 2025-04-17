from gtts import gTTS 
import pyttsx3
import os

def starting(x,filename):
    obj = gTTS(text=x , lang = 'en')
    obj.save(filename)
def endgame(x):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    
    engine.say(x)
    engine.runAndWait()
    # Convert text to speech and play it
x = input("Enter your text:")
filename = "example2.mp3"
starting(x, filename)
endgame(x)




