import requests 
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv

def get_links():
    links = []
    with open('links.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter='\n')
        for row in csv_reader:
            link = ''.join(map(str, row))
            links.append(link)
    return links

def scrape_html(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else: return None
    except RequestException as e:
        log_error('Error during requsts to {} : {}'.format(url, e))

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > 1)

def log_error(e):
    """
    Prints out the error
    """
    print(e)

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
