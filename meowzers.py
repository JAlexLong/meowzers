#!/usr/bin/env python3
import json
import os
import requests
import datetime
from dotenv import load_dotenv, find_dotenv
from PIL import Image

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("Could not find a valid api key. Exiting...")
    exit(1)


def get_cat_url():
    """Scrapes the urls of images from a webpage."""
    base_url = 'https://api.thecatapi.com/v1/images/search?api_key='
    url = base_url + API_KEY
    response = requests.get(url)
    content = json.loads(response.content)[0]
    return content['url']

def download_cat(cat):  # add -> os.Path to return name of file
    response = requests.get(cat)  # gets file data in binary form
    today = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    filename = today + ".jpg"
    filepath = os.path.join('cats', filename)
    with open(filepath, "wb") as file:
        file.write(response.content)
    return filename

def show_cat(cat):
    catname = 'cats/'+cat
    image = Image.open(catname)
    image.show()
    return True

def main():
    cat = get_cat_url()
    if not os.path.exists('cats'):
        os.mkdir('cats')
    cat_filename = download_cat(cat)
    show_cat(cat_filename)

if __name__ == "__main__":
    main()
