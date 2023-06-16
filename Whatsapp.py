from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.speak import Speak
import pathlib
from Body.listen import MicExecution
from selenium.webdriver.support.ui import WebDriverWait

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "Database\\chromedriver.exe"

#moving below two lines inside WhatsappSender function (otherwise when this library is called inside Jarvis.py, a chrome window will open up)
# driver = webdriver.Chrome(PathofDriver,options=options) 
# driver.maximize_window()


#driver.get("https://web.whatsapp.com/")
#wait = WebDriverWait(driver, 60000)
#Speak("Initializing The Whatsapp Software.")

ListWeb = {'akshay' : "+919307387494",
            'arjun': "+919400998808",
            "deepu": "+917736388256",
            "thomas": "+917034381773"}

def WhatsappSender(Name):
    driver = webdriver.Chrome(PathofDriver,options=options)
    driver.maximize_window()

    Speak("Initializing The Whatsapp Software.")
    driver.get("https://web.whatsapp.com/")
    sleep(4)
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    test1 = driver.get(LinkWeb)
    #print(str(test1))
    
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
        #test = driver.find_element(by=By.CLASS_NAME, value="tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq")
        #print(str(test))
        #test.click()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")

#WhatsappSender("deepu")
