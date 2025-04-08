import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input
def input_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            instruction = listener.recognize_google(audio)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "").strip()
                return instruction
    except Exception as e:
        print("Error:", e)
    return None

# Main function to run assistant
def play_jarvis():
    talk("Hello! I am Jarvis. How can I help you?")
    while True:
        instruction = input_instruction()
        if instruction:
            print("User:", instruction)

            if "play" in instruction:
                song = instruction.replace('play', "").strip()
                talk("Playing " + song)
                pywhatkit.playonyt(song)

            elif "time" in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk("The current time is " + time)

            elif "date" in instruction:
                date = datetime.datetime.now().strftime('%d/%m/%Y')
                talk("Today's date is " + date)

            elif "how are you" in instruction:
                talk("I am fine. How about you?")

            elif "what is your name" in instruction:
                talk("I am Jarvis, your voice assistant.")

            elif "who is" in instruction:
                person = instruction.replace("who is", "").strip()
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)

            elif "search" in instruction:
                query = instruction.replace("search", "").strip()
                talk("Searching for " + query)
                webbrowser.open(f"https://www.google.com/search?q={query}")

            else:
                talk("Sorry, I didn't catch that. Please repeat.")

# Run the assistant
if __name__ == "__main__":
    play_jarvis()
