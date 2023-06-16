#pip install googletrans==3.1.0a0
import speech_recognition as sr
from googletrans import Translator

#step 1: Listen in a language
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #listens in 8 sec sessions

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en") #ml for malayalam
        
    except:
        return ""
    
    query = str(query).lower()
    return query

#Step 2: Translate to default(english)

def Translation(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You: {data}.")
    return data

#Step 3: Connect

def MicExecution():
    query = Listen()
    data = Translation(query)
    return data

#print(Listen())
#Translation("नमस्ते क्या हाल है")
#MicExecution()
