import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

class VoiceAssistant:
    def __init__(self, name="Jarvis"):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.name = name.lower()

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def input_instruction(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.listener.adjust_for_ambient_noise(source)
                audio = self.listener.listen(source)
                instruction = self.listener.recognize_google(audio)
                instruction = instruction.lower()
                if self.name in instruction:
                    instruction = instruction.replace(self.name, "").strip()
                    return instruction
        except sr.UnknownValueError:
            self.talk("Sorry, I did not catch that.")
        except sr.RequestError:
            self.talk("Sorry, my speech service is down.")
        except Exception as e:
            print("Error:", e)
        return None

    def process_instruction(self, instruction):
        if "play" in instruction:
            song = instruction.replace('play', "").strip()
            self.talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif "time" in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.talk("The current time is " + time)
        elif "date" in instruction:
            date = datetime.datetime.now().strftime('%d/%m/%Y')
            self.talk("Today's date is " + date)
        elif "how are you" in instruction:
            self.talk("I am fine. How about you?")
        elif "what is your name" in instruction:
            self.talk(f"I am {self.name.capitalize()}, your voice assistant.")
        elif "who is" in instruction:
            person = instruction.replace("who is", "").strip()
            info = wikipedia.summary(person, 1)
            print(info)
            self.talk(info)
        elif "search" in instruction:
            query = instruction.replace("search", "").strip()
            self.talk("Searching for " + query)
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            self.talk("Sorry, I didn't catch that. Please repeat.")

    def run(self):
        self.talk(f"Hello! I am {self.name.capitalize()}. How can I help you?")
        while True:
            instruction = self.input_instruction()
            if instruction:
                print("User:", instruction)
                self.process_instruction(instruction)

if __name__ == "__main__":
    assistant = VoiceAssistant("Jarvis")
    assistant.run()
