import streamlit as st
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis talk
def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text  # Return text for UI display

# Function to recognize speech input
def recognize_speech():
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Speech Recognition service error."

# Function to handle user commands
def handle_command(command):
    response = ""
    
    if "play" in command:
        song = command.replace('play', "").strip()
        response = f"Playing {song}"
        pywhatkit.playonyt(song)

    elif "time" in command:
        response = f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

    elif "date" in command:
        response = f"Today's date is {datetime.datetime.now().strftime('%d/%m/%Y')}"

    elif "who is" in command:
        person = command.replace('who is', "").strip()
        try:
            response = wikipedia.summary(person, sentences=1)
        except wikipedia.exceptions.DisambiguationError:
            response = "There are multiple matches for this query. Could you be more specific?"
        except wikipedia.exceptions.PageError:
            response = "Sorry, I couldn't find any information on that."

    elif "search" in command:
        query = command.replace('search', "").strip()
        response = f"Searching for {query}"
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "open" in command:
        website = command.replace('open', "").strip()
        response = f"Opening {website}"
        webbrowser.open(f"http://{website}.com")

    elif "joke" in command:
        response = "Why don’t skeletons fight each other? Because they don’t have the guts!"

    elif "exit" in command or "stop" in command:
        response = "Goodbye! Have a great day."

    else:
        response = "I didn't understand that. Please say it again."

    talk(response)
    return response

# Streamlit UI
st.title("Jarvis - Voice Assistant")
st.sidebar.title("Menu")
menu = ["Home", "Conversation History", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Click the button and speak your command.")

    if st.button("Start Listening"):
        command = recognize_speech()
        st.write(f"**You:** {command}")
        if command:
            response = handle_command(command)
            st.write(f"**Jarvis:** {response}")

elif choice == "Conversation History":
    st.write("Conversation history will be displayed here.")

elif choice == "About":
    st.write("Jarvis is a simple AI assistant built with Python and Streamlit.")

