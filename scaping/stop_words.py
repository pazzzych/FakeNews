from scrape_links import (scrape_links_Obozrevatel, scrape_links_Glavcom, scrape_links_Gordon, 
                          scrape_links_NewsOne, scrape_links_Pravda, scrape_links_rbc, scrape_links_Unian)
from getting_data import scrape_data
import csv 

stop_words = []

def words_to_csv(words):
        with open('words.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='\n')
            writer.writerow(words)

def get_stop_words():
        text = get_text(scrape_links_Obozrevatel())
        freq(text, len(scrape_links_Obozrevatel()))

        text = get_text(scrape_links_Glavcom())
        freq(text, len(scrape_links_Glavcom()))

        text = get_text(scrape_links_Gordon())
        freq(text, len(scrape_links_Gordon()))

        text = get_text(scrape_links_NewsOne())
        freq(text, len(scrape_links_NewsOne()))

        text = get_text(scrape_links_Pravda())
        freq(text, len(scrape_links_Pravda()))

        text = get_text(scrape_links_rbc())
        freq(text, len(scrape_links_rbc()))

        text = get_text(scrape_links_Unian())
        freq(text, len(scrape_links_Unian()))

        return stop_words


def get_text(urls):
        text = ''
        for url in urls:
                text+=scrape_data(url)[1]
        return text

def freq(text, length):
        text_list = text.split(' ')
        unique_words = set(text_list)
        for word in unique_words:
                if text_list.count(word) >= (length//4):
                        #print(word, ':' , text_list.count(word))
                        stop_words.append(word)

words_to_csv(get_stop_words())