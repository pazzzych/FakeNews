import pymorphy2
import nltk
import re

morph = pymorphy2.MorphAnalyzer()

def lemmatize(text):
    text = re.sub(r'[^\w\s]', '', text)
    words = nltk.word_tokenize(text)

    res = []

    for word in words:
        p = morph.parse(word)[0]
        if not 'ADJF' in p.tag:
            p = p.make_agree_with_number(1).word
            p = morph.parse(word)[0]
            p = p.normal_form 
            res.append(p)

    return res 
    

