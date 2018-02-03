#!/usr/bin/env python
import feedparser # pip install feedparser
import ssl
from bs4 import BeautifulSoup

# prevent "certificate verify failed" error
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

j=1

# beardedgenderqueer has 5 pages as of Jan 31 2018
for i in range(1,6):

    d = feedparser.parse('https://beardedgenderqueer.wordpress.com/home/blog/feed/?paged='+str(i))
    # .. skipped handling http errors, cacheing ..

    # output each posts to file
    for e in d.entries:

        file = open("BeardedGQ/" + str(j) + ".txt", "w")

	    # TODO: format output into something less gross, maybe a dict?
        file.write(e.title + "\n")
        file.write(e.published + "\n")
        file.write(e.link + "\n")
        for f in e.tags:
            file.write(f.term + " ")
        file.write("\n")
    
        # strip extra whitespace, newlines
        soup = BeautifulSoup(e.content[0].value, "lxml")
    
        text = soup.get_text().strip().rstrip()
        text = text.replace("\t", "").replace("\r", "").replace("\n", " ")
    
        file.write(text + "\n")
        #print(e.keys())
        file.write(d.feed.title)
        #print("\n") # 2 newlines
        file.close()
        
        j+=1

        #keys = ['title', 'title_detail', 'links', 'link', 'comments', 'published', 'published_parsed', 'authors', 'author',
        # 'author_detail', 'tags', 'id', 'guidislink', 'summary', 'summary_detail', 'content', 'wfw_commentrss', 'slash_comments',
        # 'media_content']