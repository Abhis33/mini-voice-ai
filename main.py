import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("Recording saved as", filename)

from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # loads variables from .env into environment

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(filename):
    with open(filename, "rb") as f:
        transcript = client.audio.transcriptions.create(
            file=f,
            model="gpt-4o-transcribe"
        )
    return transcript.text

def get_llm_response(prompt, past_messages):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Past conversation - "+'\n'.join(past_messages)},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def text_to_speech(text, output_filename="output.mp3"):
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        input=text,
        voice="alloy"
    )
    with open(output_filename, "wb") as f:
        f.write(response.content)  # FIXED: use .content to get bytes
    print("Speech saved as", output_filename)

import pygame

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    print("Welcome to your Mini Voice AI Assistant. Say 'bye' to exit.\n")

    past_messages = []
    while True:
        audio_file = "input.wav"
        record_audio(audio_file, duration=5)
        
        text = transcribe_audio(audio_file)
        print("You said:", text)
        
        if "bye" in text.lower():
            print("Assistant: Goodbye!")
            break
        
        past_messages.append("USER: "+text)

        response = get_llm_response(text, past_messages)

        past_messages.append("SYSTEM: "+response)
        print("Assistant:", response)
        
        tts_file = "response.mp3"
        text_to_speech(response, tts_file)
        play_audio(tts_file)
