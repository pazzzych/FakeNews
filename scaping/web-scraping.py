import requests 
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv

def get_html(url):
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


def get_links():
    url = 'https://www.obozrevatel.com/ukr/'
    # https://newsone.ua/news.html
    response = get_html(url)

    if response is not None:
        links = []
        html = BeautifulSoup(response, 'html.parser')
        for article in html.findAll("article"):
            for a in article.findAll('a'):
                links.append(a['href'])
        return links

    #raise Exception('Error retrieving contents at {}'.format(url))

def save_links(links):
    with open('links.csv', 'w') as file:
        writer = csv.writer(file, delimiter='\n')
        writer.writerow(links)

if __name__ == '__main__':
    links = get_links()
    save_links(links)