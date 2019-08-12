import pymongo
from pymongo import MongoClient
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

def get_stop_words():
    words = []
    with open('words.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter='\n')
        for row in csv_reader:
            word = ''.join(map(str, row))
            words.append(word)
    return words

stop_words = get_stop_words()
    
def get_docs():
    documents = []
    
    client = MongoClient('mongodb://localhost:27017/')
    db = client.fake_news
    posts = db.post
    
    for post in posts.find().limit(900):
        documents.append(post['text'])
    
    return documents

def vectorise(docs):
    vectoriser = TfidfVectorizer(stop_words=stop_words, max_features=10000, max_df = 0.5, use_idf = True, ngram_range=(1,3))
    X = vectoriser.fit_transform(docs)
    print('SHAPE OF X:', X.shape)
    terms = vectoriser.get_feature_names()
    return X, terms


# clustering w/ KMeans
from sklearn.cluster import KMeans

def clustering_KMeans(X):
    num_clusters = 5
    km = KMeans(n_clusters=num_clusters)
    km.fit(X)
    clusters = km.labels_.tolist()
    return clusters


docs = get_docs()
X, terms = vectorise(docs)
clusters = clustering_KMeans(X)
print(clusters)
#lsa(X)

from sklearn.utils.extmath import randomized_svd
U, Sigma, VT = randomized_svd(X, n_components=5, n_iter=1000, random_state=122)
#printing the concepts
for i, comp in enumerate(VT):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
    print("Concept "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])
        print(" ")

import umap
X_topics=U*Sigma
embedding = umap.UMAP(n_neighbors=50, min_dist=0.5, random_state=12).fit_transform(X_topics)
plt.figure(figsize=(10, 10))
plt.scatter(embedding[:, 0], embedding[:, 1], 
                c = clusters,
                s = 10, # size
                edgecolor='none'
                )
plt.show()