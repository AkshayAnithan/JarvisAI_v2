import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from ScreenReader.download import *
from ScreenReader.caption import caption_generator

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)


def get_contents(link):
    # Step 1: Start a Selenium WebDriver
    #driver = webdriver.Firefox()
    driver.get(link)

    # Step 2: Retrieve the webpage source
    page_source = driver.page_source

    # Step 3: Parse contents of webpage
    soup = BeautifulSoup(driver.page_source, "html.parser")

    #Step 4: Iterate through body tags and get contents
    document = ''
    body_tag = soup.body
    document = extract_contents(link, body_tag, document)


    #Step 5: Create the file
    title_tag = soup.title
    with open('extracted.txt', 'w', encoding="utf8") as f:
        f.write("The title of the webpage is \"" + title_tag.get_text() + "\".\n")
        f.write("The contents of the webpage are as follows: \n\n")
        f.write(document)
    
    # Step 6: Close the WebDriver
    driver.quit()
    return document

def extract_contents(link, root_tag, document):
    explore_list = ["div"]
    exclusion_list = ["b", "center", "strong", "script", "style"]
    appended_strings = set()  # Set to store previously appended strings

    for tag in root_tag.descendants:
        if isinstance(tag, str):
            content_string = tag.get_text().strip()
        #     continue
        # if tag.name in explore_list:
        #     continue
        # elif tag.name not in exclusion_list:
        #     if tag.name == "img":
        #         if 'aria-label' in tag.attrs:
        #             name = tag['aria-label']
        #         elif 'alt' in tag.attrs:
        #             name = tag['alt']
        #         else:
        #             image_path = extract_image(link, tag['src'])
        #             name = caption_generator(image_path)
        #         if name:
        #             content_string = "The webpage contains an image of a " + name + " here."
        #         else:
        #             content_string = "The webpage contains an image here."
        #     elif tag.name == "ol" or tag.name == "ul":
        #         if tag.name == "ol":
        #             content_string = "Ordered List:"
        #         elif tag.name == "ul":
        #             content_string = "Unordered List:"
        #         i = 1
        #         for item in tag.children:
        #             if item.name == "li":
        #                 if tag.name == "ol":
        #                     content_string += "\n\tElement "
        #                 elif tag.name == "ul":
        #                     content_string += "\n\tBullet Point "
        #                 content_string += str(i)
        #                 i = i + 1
        #                 content_string += ": " + item.get_text()
        #     elif tag.name == "form":
        #         content_string = "The webpage contains a form with "

        #         descendants_list = list(tag.descendants)

        #         for i, item in enumerate(descendants_list):
        #             if item is None or not item.name:  # Check if item is None or does not have a name attribute
        #                 continue
        #             if item.name != "input":
        #                 if item.name == "label":
        #                     continue
        #                 if item.name[0] in ['a', 'e', 'i', 'o', 'u']:
        #                     name = "an "
        #                 else:
        #                     name = "a "
        #                 name += item.name
        #                 if item.get("name"):
        #                     name += " named \"" + item["name"] + "\""
        #                 if i != len(descendants_list) - 1:
        #                     name += ", "
        #                 else:
        #                     name += "."
        #             else:
        #                 if item.get("type"):
        #                     if item["type"][0] in ['a', 'e', 'i', 'o', 'u']:
        #                         name = "an "
        #                     else:
        #                         name = "a "
        #                     name += item["type"]
        #                     if item.get("name"):
        #                         name += " named \"" + item["name"] + "\""
        #                     if descendants_list[i + 1].name == "label":
        #                         name += " labelled \"" + descendants_list[i + 1].get_text() + "\""
        #                     if i != len(descendants_list) - 1:
        #                         name += ", "
        #                     else:
        #                         name += "."
        #             content_string += name
        #     else:
        #         content_string = tag.get_text().strip()

            if content_string not in appended_strings and len(content_string) > 40:
                document += "\n"
                document += content_string
                appended_strings.add(content_string)

    return document

# website_link = input("Website Link: ")
# get_contents(website_link)

