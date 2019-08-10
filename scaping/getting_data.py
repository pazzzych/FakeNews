import requests 
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv
from scrape import scrape_html

def get_links():
    links = []
    with open('links.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter='\n')
        for row in csv_reader:
            link = ''.join(map(str, row))
            links.append(link)
    return links

def scrape_data(url):
    response = scrape_html(url)

    title = ''
    text = ''

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for h1 in html.findAll("h1"):
            title = h1.text.replace('\n', '')
        for parag in html.findAll("p"):
                text += parag.text
        
    
    return [title, text]
