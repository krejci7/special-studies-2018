#!/usr/bin/env python
import feedparser # pip install feedparser
import ssl
from bs4 import BeautifulSoup
import json
import datetime
import re
import calendar

# define dictionary of month abbreviations : month number
monthint = {v: k for k,v in enumerate(calendar.month_abbr)}

# prevent "certificate verify failed" error
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# for naming output files
j=1

# genderkid has 14 pages as of Feb 15 2018
for i in range(1,15):

    d = feedparser.parse('https://genderkid.wordpress.com/feed/?paged='+str(i))
    # .. skipped handling http errors, cacheing ..

    # output each post to file
    for e in d.entries:

        post = {}

	    # format output into a dict
        post['title'] = e.title
        post['date'] = e.published

        # save date as an "object"
        year = int(re.findall(r'\d{4}', e.published)[0])
        months = re.findall(r'\w{3}', e.published)[1]
        month = monthint[months]
        day = int(re.findall(r'\d{2}', e.published)[0])
        date = str(datetime.date(year, month, day))
        post['dateobj'] = date

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
        file = open("RawPosts/genderkid/" + str(j) + ".txt", "w")
        file.write(json.dumps(post))
        file.close()
        
        j+=1

        #keys = ['title', 'title_detail', 'links', 'link', 'comments', 'published', 'published_parsed', 'authors', 'author',
        # 'author_detail', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments',
        # 'media_content']