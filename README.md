from gtts import gTTS
import os
import pyttsx3

def text_to_speech(text, filename):
    """
    Convert text to speech and save as an MP3 file.

    Args:
        text (str): The text to convert to speech.
        filename (str): The filename to save the MP3 file.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang='en')

    # Save the MP3 file
    tts.save(filename)

def speak_text(text):
    """
    Convert text to speech and play it immediately.

    Args:
        text (str): The text to convert to speech.
    """
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the speech rate
    engine.setProperty('rate', 150)

    # Convert text to speech and play it
    engine.say(text)
    engine.runAndWait()

# Example usage
text = input("Enter your text:")
filename = "example3.mp3"

# Convert text to speech and save as an MP3 file
text_to_speech(text, filename)

# Convert text to speech and play it immediately
speak_text(text)
