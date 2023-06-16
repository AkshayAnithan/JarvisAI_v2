from ScreenReader.summarize import *
from ScreenReader.extract import *
from ScreenReader.chunkify import *
from ScreenReader.handleTags import *
from bs4 import BeautifulSoup
from selenium import webdriver

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
'''
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)



tag_index = -1
tag_list = []

def read_webpage(link):
    # Step 1: Start a Selenium WebDriver
    #driver = webdriver.Firefox()
    driver.get(link)

    # Step 2: Retrieve the webpage source
    page_source = driver.page_source

    # Step 3: Create the List
    soup = BeautifulSoup(driver.page_source, "html.parser")
    inclusion_list = ["title", "h1", "h2", "h3", "h4", "h5", "h6", "p", "img"]
    tag_list = soup.find_all(lambda tag: tag.name in inclusion_list and tag.get("aria-hidden") != "true" and tag.get("style") != "display:none" and tag.get("style") != "visibility:hidden")
    
    # Step 4: Close the WebDriver
    driver.quit()

    # Step 5: Read the contents aloud
    handle_tags(link, tag_list)

def handle_tags(link, tag_list):
    say("Would you like to enable option to navigate to other links? ")
    link_nav = listen()
    for tag in tag_list:
        tag_name = tag.name
        # accessible_name = computeAccessibleName(tag)

        if tag_name == "title":
            announcement = f"Title of Webpage, {tag.contents[0]}"
            say(announcement)
        elif tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            announcement = f"Heading Level {int(tag.name[1])}: {tag.get_text().strip()}"
            say(announcement)
        elif tag_name == "img":
            if 'aria-label' in tag.attrs:
                img_name = tag['aria-label']
            elif 'alt' in tag.attrs:
                img_name = tag['alt']
            else:
                image_path = extract_image(link, tag['src'])
                img_name = caption_generator(image_path)
            if img_name:
                announcement = "The webpage contains an image of a " + img_name + " here."
            else:
                announcement = "The webpage contains an image."
            say(announcement)
        elif tag.name == "p":
            tag_text = tag.get_text().strip()
            chunks = split_document(tag_text, 15)
            for chunk in chunks:
                say(chunk)

            if link_nav == "yes":
                num = len(tag.find_all("a"))
                if num > 0:
                    say("The paragraph contains " + str(num) + "tags. They are as follows: ")
                for child_tag in tag.descendants:
                    if child_tag.name == 'a':
                        link_text = handle_links(child_tag)
                        say(link_text)
                        if link_text.startswith("Would you like to move to"):
                            choice = listen()
                            if choice == "yes":
                                from chunkSR import start_chunkSR
                                start_chunkSR(link)

