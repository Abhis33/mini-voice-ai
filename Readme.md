# 🗣️ Mini Voice AI Assistant

## 📖 Description

This is a **simple voice-based AI assistant** that:

1. Records your voice.
2. Transcribes speech to text using **gpt-4o-transcribe**.
3. Generates a response using **gpt-4.1**.
4. Converts the response to speech using **gpt-4o-mini-tts**.
5. Plays the audio reply back to you.

🔁 The assistant runs in a loop for **multi-turn conversation**, exiting when you say "bye".

---

## 🚀 Features

- ✅ Record audio from microphone.
- ✅ Transcribe audio to text via OpenAI Whisper.
- ✅ Generate conversational responses via LLM.
- ✅ Convert text responses to speech.
- ✅ Play audio replies in real-time.
- ✅ Supports multi-message conversational loop.

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

```
git clone https://github.com/abhis33/mini-voice-ai.git
cd mini-voice-ai
```

2. **Create a .env file in the project root:**

```
OPENAI_API_KEY="your_openai_api_key_here"
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Run the assistant:**

```
python main.py
```

## Usage Example

```
$ python main.py
Welcome to your Mini Voice AI Assistant. Say 'bye' to exit.

Recording...
Recording saved as input.wav
You said: What's the time in Tokyo?
Assistant: The current time in Tokyo is 2:30 PM.

Recording...
Recording saved as input.wav
You said: bye
Assistant: Goodbye!
```

## Additional Features (Future Improvements)
🔊 Adjustable recording durations or manual start/stop recording controls.

🌐 Web UI using Flask + JavaScript:

Record button

Playback controls

Display transcriptions and AI replies dynamically

🧠 Contextual memory:

Maintain conversation history for coherent multi-turn dialogue.

🎙️ Streaming responses:

Partial speech playback as LLM generates responses (more natural conversation).

🔒 Authentication and user management for multi-user setups.

🤖 Intent recognition:

Handle different commands, tasks, and actions.

## WebSocket Integration for Real-time Dialogue

#### Why?
Currently, each interaction is request-response based (record → process → play). For real-time streaming dialogue, integrate WebSockets to:

Stream audio chunks to backend continuously.

Perform on-the-fly transcription with partial outputs.

Send partial or final transcriptions to LLM instantly.

Stream back TTS audio in chunks to client for immediate playback.

##### Implementation Idea
Use FastAPI with WebSocket endpoints.

On frontend:

Use JavaScript Web Audio API to stream mic input.

Connect to backend WebSocket.

On backend:

Stream audio to Whisper for partial transcriptions.

Send partial text to GPT for incremental responses.

Stream TTS audio back to client for playback.

✅ This approach mimics real-time assistants like Alexa or Google Assistant with low latency and natural flow.

## 📝 License
MIT License. Feel free to use, modify, and distribute with attribution.

