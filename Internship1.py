#!/usr/bin/env python
# coding: utf-8

# In[5]:


from lxml import html
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import xlsxwriter
import re
import json

url = "https://www.instructables.com/Hydraulic-Craft-Stick-Box/"
data = requests.get(url)
soup = soup(data.content,"lxml")

for a in soup.findAll("article", {"id": "article"}):
    scraped_url=print(soup.title.text)
    header=a.find("h1")
    header_title=print(header.text)
    images = a.findAll('a', {'href':  re.compile('https')})
    for link in images:
        image_url=print(link['href']+'\n')
    youtube = a.findAll('iframe', {'src':  re.compile('https')})
    for link in youtube:
        youtube_url= (link['src']+'\n')
    view = a.find('p', {'class': "view-count"})
    view_url = print(view.text)
    favourite = a.find('p', {'class': "favorite-count"})
    favourite_url = print(favourite.text)
    comment = a.find('p', {'class': "comment-count"})
    comment_url = print(comment.text)
    steps = a.findAll('h2', {'class': "step-title"})
    for link in steps:
        step = print(link.text)
        
with open('JSONFile.txt', 'wt') as outfile:
    json.dump(scraped_url, outfile)
    json.dump(header_title,outfile)
    json.dump(image_url,outfile)
    json.dump(view_url,outfile)
    json.dump(favourite_url,outfile)
    json.dump(comment_url,outfile)
    json.dump(step,outfile)


# In[ ]:




