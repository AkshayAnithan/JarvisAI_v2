import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse


def download_image(image_url):
    # Send a GET request to download the image
    image_response = requests.get(image_url)

    # Extract the image filename from the URL
    image_filename = os.path.basename(urlparse(image_url).path)

    # Save the image to the 'images' directory
    with open(os.path.join("images", image_filename), "wb") as image_file:
        image_file.write(image_response.content)

    print(f"Downloaded: {image_filename}")
    return os.path.join("images", image_filename)


def extract_image(link, img_src):
    # Send a GET request to fetch the webpage content
    response = requests.get(link)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the <img> tag with the specified src attribute
    image_tag = soup.find("img", src=img_src)

    if image_tag:
        # Get the absolute image URL
        image_url = urljoin(link, image_tag["src"])

        # Create a directory to store the downloaded image
        if not os.path.exists("images"):
            os.makedirs("images")

        # Download the image
        image_path = download_image(image_url)
        return image_path
    else:
        print("Image not found.")
        return None


# Usage example:
# link = "https://en.wikipedia.org/wiki/Guardians_of_the_Galaxy_Vol._3"
# img_src = "/wiki/File:Guardians_of_the_Galaxy_Vol._3_logo.jpg"
# image_path = extract_image(link, img_src)
# print("Image path:", image_path)
