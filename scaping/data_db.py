from getting_data import get_links, scrape_data
from mongoengine import *

connect('fake_news', host='localhost', port=27017)

class Post(Document):
    title = StringField(required=True, max_length=200)
    text = StringField(required=True)
    category = StringField(require=True, default='Politics')
    label = IntField(default=1)

links = get_links()
for link in links:
    title, text = scrape_data(link)
    post = Post(
        title = title,
        text = text 
    )
    post.save()