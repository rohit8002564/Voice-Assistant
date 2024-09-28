import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "")
                print(instruction)
            return instruction
    except Exception as e:
        print("Error:", e)
        return None

def play_jarvis():
    while True:
        instruction = input_instruction()
        if instruction:
            print(instruction)
            if "play" in instruction:
                song = instruction.replace('play', "")
                talk("playing" + song)
                pywhatkit.playonyt(song)

            elif 'time' in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('The current time is ' + time)

            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d/%m/%Y')
                talk("Today's date is " + date)

            elif 'how are you' in instruction:
                talk('I am fine, how about you?')

            elif 'what is your name' in instruction:
                talk('I am jarvis, what can I do for you?')

            
            elif 'who is' in instruction:
                human = instruction.replace('who is', ' ')
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)

            elif 'search' in instruction:
                query = instruction.replace('search', "")
                talk("Searching for" + query)
                webbrowser.open(f"https://www.google.com/search?q={query}")

            else:
                talk('Please repeat that.')
    

        
play_jarvis()
