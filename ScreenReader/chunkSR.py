from selenium import webdriver
from bs4 import BeautifulSoup
from ScreenReader.reader  import *  #includes reader
from ScreenReader.summarize import *  #includes summarise
from ScreenReader.extract import *  #includes get_contents()
import requests


tag_index = -1
tag_list = []

#api key
fileopen = open("Data\\Api_summarize.txt","r")
API = fileopen.read()
fileopen.close()

#importing
import openai
from dotenv import load_dotenv 

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def start_chunkSR(link):
    # say("Shall I provide a summary of the webpage contents?")
    # choice = listen()
    # if choice == "yes":
    #     contents = get_contents(link)
    #     webpage_content = summarise()
    #     say(webpage_content)
    #     return
    # else:
    #     read_webpage(link)
    
    webpage_contents = get_contents(link)
    
    summarise(webpage_contents)
    
    return ''



def initiate_chunkSR():
    start_chunkSR('https://www.wikipedia.com/wiki/internet')
    

