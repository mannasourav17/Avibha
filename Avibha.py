
import speech_recognition as s
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes




listener = s.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
   
    try:
    
        
        with s.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.rreplace('alexa', '')
                print(command)
    except:
       
        pass
    return command


def run_alexa():
    commands = take_command()
    print(commands)
    if 'play' in commands:
        song = commands.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in commands:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in commands:
        person = commands.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in commands:
        talk('sorry, I have a headache')
    elif 'are you single' in commands:
        talk('I am in a relationship with wifi')
    elif 'joke' in commands:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()