import requests 
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv

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


def scrape_links():
    url = 'https://www.obozrevatel.com/ukr/'
    response = scrape_html(url)
    links = []

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for article in html.findAll("article"):
            for a in article.findAll('a'):
                links.append(a['href'])

    return list(set(links))

def clean_links(links):
    for link in links:
        if link.endswith('/'):
            links.remove(link)

    forbidden = ['/show/', '/person/', '/astro/', '/society/', '/kiyany/', '/moyashkola/']

    for link in links:
        for forb in forbidden:
            i = 0
            while i < len(links):
                if forb in link:
                    links.remove(links) 

    return links

def links_to_csv(links):
    with open('links.csv', 'a') as file:
        writer = csv.writer(file, delimiter='\n')
        writer.writerow(links)

if __name__ == '__main__':
    links = clean_links(scrape_links())
    links_to_csv(links)