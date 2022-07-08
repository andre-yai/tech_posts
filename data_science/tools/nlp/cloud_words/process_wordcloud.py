import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np


currdir = os.path.dirname(__file__)

def get_WikiPage(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wordCloud(text, mask_image_name, export_image_name):

    mask = np.array(Image.open(os.path.join(currdir,mask_image_name)))

    stopwords = set(STOPWORDS)

    wc = WordCloud(background_color='white', 
                  mask=mask,
                  max_words=200,
                  stopwords=stopwords)

    wc.generate(text)

    wc.to_file(os.path.join(currdir,export_image_name))

# TODO: Get from other text sources.
page_name = "Coronavirus Brazil"
mask_image_name = 'Brazil.png'
export_image_name = "corona_brazil_wc.png"
text = get_WikiPage(page_name)
create_wordCloud(text,mask_image_name, export_image_name)
