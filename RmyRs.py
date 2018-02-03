#!/usr/bin/env python
import feedparser # pip install feedparser
import ssl
import requests
from bs4 import BeautifulSoup

# prevent "certificate verify failed" error
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

j=1

# Raising My Rainbow has 33 pages as of Feb 03 2018
for i in range(1,34):

    d = feedparser.parse('https://raisingmyrainbow.com/feed/?paged='+str(i))
    # .. skipped handling http errors, cacheing ..

    # output each posts to file
    for e in d.entries:

        file = open("RmyR/" + str(j) + ".txt", "w")

	    # TODO: format output into something less gross, maybe a dict?
        file.write(e.title + "\n")
        file.write(e.published + "\n")
        file.write(e.link + "\n")
        for f in e.tags:
            file.write(f.term + " ")
        file.write("\n")

        #print(e.keys())
    
        # strip text from full post link
        url = e.link
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")
        text = soup.find(attrs={"class": "entry-content"}).get_text()

        # remove Advertisements code
        text = text.split("Advertisement")
        text = text[0].replace("\t", "").replace("\r", "").replace("\n", " ")

        file.write(text)
    
        #print(text + "\n")
        #print(e.keys())
        #print(d.feed.title)
        #print("\n") # 2 newlines
        file.close()
        
        j+=1

        #keys = ['title', 'title_detail', 'links', 'link', 'comments', 'published', 'published_parsed', 'authors', 'author',
        # 'author_detail', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments',
        # 'media_content']