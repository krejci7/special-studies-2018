#!/usr/bin/env python
import feedparser # pip install feedparser
import ssl
from bs4 import BeautifulSoup
import json

# prevent "certificate verify failed" error
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# for naming output files
j=1

# Born Wrong has 4 pages as of Feb 15 2018
for i in range(1,5):

    d = feedparser.parse('https://b0rnwr0ng.wordpress.com/feed/?paged='+str(i))
    # .. skipped handling http errors, cacheing ..

    # output each post to file
    for e in d.entries:

        post = {}

	    # format output into a dict
        post['title'] = e.title
        post['date'] = e.published
        post['link'] = e.link
        post['tags'] = []
        for f in e.tags:
            post['tags'].append(f.term)
    
        # strip extra whitespace, newlines
        soup = BeautifulSoup(e.content[0].value, "lxml")
    
        text = soup.get_text().strip().rstrip()
        text = text.replace("\t", "").replace("\r", "").replace("\n", " ")
    
        post['text'] = text
        post['feedtitle'] = d.feed.title
        file = open("RawPosts/BornWrong/" + str(j) + ".txt", "w")
        file.write(json.dumps(post))
        file.close()
        
        j+=1

        #keys = ['title', 'title_detail', 'links', 'link', 'comments', 'published', 'published_parsed', 'authors', 'author',
        # 'author_detail', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments',
        # 'media_content']