#!/usr/bin/env python3
import json
import os
import requests
import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

def create_directory(name):
    """Checks if the directory exists and then creates it if it doesn't"""
    directory_name = name
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    return directory_name

def get_cat_url():
    """Scrapes the urls of images from a webpage."""
    base_url = 'https://api.thecatapi.com/v1/images/search?api_key='
    url = base_url + API_KEY
    response = requests.get(url)
    content = json.loads(response.content)[0]
    return content['url']

def download_cat(cat, download_location=os.getcwd()):
    response = requests.get(cat)  # gets file data in binary form
    today = str(datetime.datetime.now().strftime("%Y%m%d"))
    filename = today + ".jpg"
    filepath = os.path.join(download_location, filename)
    with open(filepath, "wb") as file:
        file.write(response.content)

def main():
    cat = get_cat_url()
    data_directory = create_directory('data')
    download_cat(cat, data_directory)
    print(cat)
    print(os.getcwd())

if __name__ == "__main__":
    main()
