#Speak function 2 types: 1] windows based 2] Chrome based
'''
For windows based
pip install pyttsx3
pip install selenium==4.1.3

Features:
fast and offline

Cons:
Cant interrupt while speaking
less choice for voice
'''
# import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices',voices[1].id)
#     engine.setProperty('rate',170)  #1x=200 2x=400(?)
#     print("")
#     print(f"You: {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()
    
# Speak("Hello Sir")

'''
Chrome based

Features:
More voices
More clear
Can listen while speaking 

Cons:
word limit
little slow
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
#driver = webdriver.Chrome()
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lengthoftext = len(str(Text))
    
    if lengthoftext==0:
        pass
    else:
        print("")
        print(f"AI: {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthoftext <=10:
            sleep(2) 

        elif lengthoftext <= 30:
            sleep(4)

        elif lengthoftext <= 40:
            sleep(6)
            
        elif lengthoftext <= 55:
            sleep(8)

        elif lengthoftext <= 70:
            sleep(10)
            
        elif lengthoftext <= 100:
            sleep(13)
            
        elif lengthoftext > 100:
            sleep(14)    
            
        else:
            sleep(2)
             

#Speak("HEy akshay")