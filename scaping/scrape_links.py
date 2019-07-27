from bs4 import BeautifulSoup
from scrape import scrape_html
import csv

def scrape_links_Obozrevatel():
    url = 'https://www.obozrevatel.com/ukr/'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for article in html.findAll("article"):
            for a in article.findAll('a'):
                links.append(a['href'])

    for link in links:
        if link.endswith('/'):
            links.remove(link)

    return list(set(links))

def scrape_links_Unian():
    url = 'https://www.unian.ua/detail/main_news'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for div in html.findAll('div', {'class':'gallery-item news-inline-item'}):
            for a in div.findAll('a'):
                links.append(a['href'])

    return list(set(links))

def scrape_links_Pravda():
    url = 'https://www.pravda.com.ua/news/'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for div in html.findAll('div', {'class':'article'}):
            for a in div.findAll('a'):
                if not a['href'].startswith('https'):
                    links.append('https://www.pravda.com.ua'+a['href'])

    return list(set(links))

def scrape_links_NewsOne():
    url = 'https://newsone.ua/news.html'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for h2 in html.findAll('h2'):
            for a in h2.findAll('a'):
                links.append('https://www.newsone.ua'+a['href'])

    return list(set(links))

def scrape_links_Glavcom():
    url = 'https://glavcom.ua/news.html'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for ul in html.findAll('ul', {'class':'list'}):
            for a in ul.findAll('a'):
                links.append('https://glavcom.ua'+a['href'])

    return list(set(links))

def scrape_links_rbc():
    url = 'https://www.rbc.ua/rus/news'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for div in html.findAll('div', {'class':'content-section'}):
            for a in div.findAll('a'):
                links.append(a['href'])

    return list(set(links))

def scrape_links_Gordon():
    url = 'https://gordonua.com/ukr/news.html'
    links = []
    response = scrape_html(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for div in html.findAll('div', {'class':'lenta_head'}):
            for a in div.findAll('a'):
                links.append('https://gordonua.com'+a['href'])

    return list(set(links))


def links_to_csv(links):
    with open('links.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter='\n')
        writer.writerow(links)
    

if __name__ == '__main__':
    links = scrape_links_Glavcom()
    links_to_csv(links)
    links = scrape_links_Gordon()
    links_to_csv(links)
    links = scrape_links_NewsOne()
    links_to_csv(links)
    links = scrape_links_Obozrevatel()
    links_to_csv(links)
    links = scrape_links_Pravda()
    links_to_csv(links)
    links = scrape_links_rbc()
    links_to_csv(links)
    links = scrape_links_Unian()
    links_to_csv(links)