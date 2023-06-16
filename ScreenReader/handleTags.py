import requests
from ScreenReader.summarize import *
from bs4 import BeautifulSoup

# #This function announces the element
# def announceElement(element):
#     role = computeRoles(element)
#     getAnnouncement(element)
    

# #This function returns different announcements for different tags
# def getAnnouncement(element):
#     tag_name = element.name
#     accessible_name = computeAccessibleName(element)

#     if tag_name == "title":
#         announcement = f"Page, {element.contents[0]}"
#     elif tag_name == "a":
#         announcement = f"Link, {accessible_name}. To follow the link, press Enter key."
#     elif tag_name == "button":
#         announcement = f"Button, {accessible_name}. To press the button, press Space key."
#     elif tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
#         level = element.attrs.get("aria-level", tag_name[1])
#         announcement = f"Heading level {level}, {accessible_name}"
#     elif tag_name == "p":
#         announcement = element.contents
#     elif tag_name == "img":
#         announcement = f"Image, {accessible_name}"
#     else:
#         announcement = f"{tag_name} element: {accessible_name}"

#     say(announcement)


# This function computes name of element as understandable by visually impaired person
def computeAccessibleName(element):
    content = element.get_text().strip()

    if 'aria-label' in element.attrs:
        return element['aria-label']
    elif 'alt' in element.attrs:
        return element['alt']
    else:
        return content

# This function computes role of element
def computeRoles(element):
       name = element.name.lower()
       if 'role' in element.attrs:
            return element['role']
       return mappings(name)

#This function maps roles to some tags
def mappings(tag):
    if tag == "a":
        return "link"
    elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        return "heading"
    elif tag == "p":
        return "paragraph"
    elif tag == "button":
        return "button"
    elif tag == "html":
        return "page"
    elif tag == "img":
        return "image"
    else:
        print("<",tag,">")
        return "default"
    
def handle_links(a_tag):
    link_url = a_tag['href']  # Get the URL from the href attribute

    # Check if the link is internal or external
    if link_url.startswith('#'):  # Internal link
        section_title = link_url[1:]  # Remove the '#' character from the URL
        return "Link points to internal section titled: " + section_title
    else:  # External link
        try:
            response = requests.get(link_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                webpage_title = soup.title.get_text().strip()
                return "Would you like to move to webpage titled \"" + webpage_title + "\"."
            else:
                return "Would you like to move to " + link_url
        except requests.exceptions.RequestException:
            return "An error occurred while accessing the webpage:" + link_url
        
