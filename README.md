# Jarvis Voice Assistant

This project is a simple voice assistant named "Jarvis," built using Python libraries like `speech_recognition`, `pyttsx3`, `pywhatkit`, `wikipedia`, `datetime`, and `webbrowser`. It listens to voice commands and can perform tasks like playing songs on YouTube, telling the time or date, searching the web, retrieving Wikipedia information, and much more.

## Features

- **Play Music**: Ask Jarvis to play a song on YouTube. Example: "Jarvis, play [song name]."
- **Tell Time**: Ask Jarvis for the current time. Example: "Jarvis, what time is it?"
- **Tell Date**: Ask Jarvis for today's date. Example: "Jarvis, what's the date?"
- **Wikipedia Search**: Ask Jarvis who someone is, and it will provide a summary from Wikipedia. Example: "Jarvis, who is [person's name]?"
- **Web Search**: Jarvis can search for anything on Google. Example: "Jarvis, search [query]."
- **Friendly Conversations**: Jarvis can answer simple questions like "How are you?" and "What is your name?"

# break
Breaking the Loop: Each time a command is executed, the loop is broken (break is used). This ensures that the command is executed only once.

For example: If you say "Play [song]", the assistant will play the song, and then the loop will stop, waiting for you to relaunch it for a new command.
Clear Interaction: For each command, once the action (such as playing a song, telling the time, or searching the web) is completed, the assistant will stop processing further until it's manually restarted.

Why This Works:

By using break, you are ensuring that after one command is processed, it doesn't repeat the same action over and over again.

## Usage:
Say "Jarvis, play [song]" → It will play the song and stop.

Say "Jarvis, what time is it?" → It will tell the time and stop.

Say "Jarvis, search for [query]" → It will search and stop.

Say "Jarvis, exit" → It will stop the assistant entirely.

## Requirements

Before running this project, you need to install the following Python libraries:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
Additionally, you might need to install PyAudio for SpeechRecognition:
pip install PyAudio
