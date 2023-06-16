
# def MainExe():
#     Speak("Main Execution has been started.")
#     while True:
#         query = Listen()
#         if "hello" in query:
#             Speak("Hi! I am Jarvis!")
            
#         elif "bye" in query:
#             Speak("Hello Bye.")

# MainExe()


from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.speak import Speak
#print(">> Initializing Jarvis....Just a moment Sir..!")
Speak("Initializing Jarvis....Just a moment Sir..!")
from Body.listen import MicExecution
from Features.Clap import Tester
print(">> Initializing Jarvis....Will be on rather soon..!")
from Main import MainTaskExecution

from FaceRecognition.recognition import FaceRecognition  #for face authentication

from os_module.os_automation import initaite_os_module
from Web_Explorer_for_IVA.main import initiate_web_explorer
from ScreenReader.chunkSR import initiate_chunkSR

goto_os_mod_commands = [
    'goto os module',
    'goto system module'
]

goto_web_mod_commands = [
    'goto web portal',
    'open web portal'
]


def MainExecution():
    
    Speak("Hello Sir..!")
    
    
    #face authentication module starts
    #to authenticate user via face recognition
    Speak("Please try to be in front of the camera for face Authentication. You can feel the keyboard and monitor of the laptop by touching it. Just keep your face upright to that!")
    try:
        fr = FaceRecognition()
        fr.run_recognition()
        Speak("User Identified...")
        Speak("I am Jarvis here, at your command sir..")
        
    except Exception as e:
        Speak('Face Authentication System Failed, but we can continue for now... and I am Jarvis here, at your command sir...')
    #face authenticaon module ends
    
    
    #Speak("I am Jarvis here, at your command.")
    
    while True:
        #Uncomment below to tell to IVA (for testing other modules for now, this is being commented out)
        #Data = MicExecution()  
        
        Data = input('Enter your command: ')
            
        Data = str(Data)
        
        ValueReturn = False
        
        #Have some confusions in the below code, so just making another one for now
        '''
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass
        
        elif len(Data)<3:
            pass
        
        elif "turn on the tv" in Data:
            Speak("Ok..Turning on the android TV..")
            
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)
            
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
        '''
        
        if any(command in Data.lower() for command in goto_os_mod_commands):
            initaite_os_module()
            
        elif any(command in Data.lower() for command in goto_web_mod_commands):
            initiate_web_explorer()
                
                
                
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
        
    
        
                
        

def ClapDetect():           #Wake word Detection
    # Speak("test1")
    # query = Tester()
    # if "True-Mic" == query:
    #     print(">>Clap Detected!! >>")
    #     print("")
    #     MainExecution()     
    # else:
    #   pass
    
    #MainExecution()
    initiate_web_explorer()
    #initiate_chunkSR()
    
    
ClapDetect()    