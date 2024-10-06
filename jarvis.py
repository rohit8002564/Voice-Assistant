import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia  # Added wikipedia import
import time  # For adding pauses

# Initialize the recognizer and text-to-speech engine
listener = aa.Recognizer()
machine = pyttsx3.init()

# Function to make Jarvis talk
def talk(text):
    machine.say(text)
    machine.runAndWait()

# Function to wish the user based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")
    talk("I am Jarvis, I am excited to chat with you how can I help you today?")

# Function to capture voice input from the user
def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            listener.adjust_for_ambient_noise(origin, duration=1)  # Adjust for background noise
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "")
                print(instruction)
            return instruction
    except Exception as e:
        print("Error:", e)
        talk("I didn't catch that, please repeat.")
        return None

# Main function to handle voice instructions
def play_jarvis():
    wishMe()  # Greet the user
    while True:
        instruction = input_instruction()
        
        if instruction:  # If instruction is not empty
            print(f"Instruction received: {instruction}")
            
            # Play a song on YouTube
            if "play" in instruction:
                song = instruction.replace('play', "")
                talk(f"Playing {song}")
                pywhatkit.playonyt(song)
            
            # Tell the current time
            elif 'time' in instruction:
                time_str = datetime.datetime.now().strftime('%I:%M %p')
                talk(f'The current time is {time_str}')
            
            # Tell today's date
            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d/%m/%Y')
                talk(f"Today's date is {date}")
            
            # Answer how Jarvis is feeling
            elif 'how are you' in instruction:
                talk("I am doing great, how about you?")
            
            # Respond to name inquiry
            elif 'what is your name' in instruction:
                talk("I am Jarvis, your personal assistant.")
            
            # Provide information about a person
            elif 'who is' in instruction:
                person = instruction.replace('who is', "")
                try:
                    info = wikipedia.summary(person, sentences=1)
                    print(info)
                    talk(info)
                except wikipedia.exceptions.DisambiguationError:
                    talk("There are multiple matches for this query. Could you be more specific?")
                except wikipedia.exceptions.PageError:
                    talk("Sorry, I couldn't find any information on that.")
                except Exception as e:
                    print(e)
                    talk("Sorry, something went wrong.")
            
            # Search Google for a query
            elif 'search' in instruction:
                query = instruction.replace('search', "")
                talk(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            
            # Open a website
            elif 'open' in instruction:
                website = instruction.replace('open', "").strip()
                url = f"http://{website}.com"
                talk(f"Opening {website}")
                webbrowser.open(url)
            
            # Tell a joke (You can enhance this by integrating a joke API)
            elif 'joke' in instruction:
                joke = " What’s the smartest insect? A spelling bee!"
                talk(joke)
            
            # Exit the assistant
            elif 'exit' in instruction or 'stop' in instruction:
                talk("Goodbye! Have a great day.")
                break  # Stop the assistant
            
            # If instruction is not understood
            else:
                talk("I didn't understand that. Please say it again.")
        
        # If no instruction was captured
        else:
            talk("Could you repeat that, please?")

# Start the assistant
play_jarvis()
