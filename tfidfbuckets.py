import nltk
import json
import re
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import os
from tfidf3 import tfidf
from tfidf3 import process

# size of sliding window
window = 30

numblogs = 1

posts = []
bucket = ""

# get blog name and number of posts for each blog
for currblog in range (1, numblogs + 1):
    blog = input("Blog name: ")
    startdate = input("Starting date (YYYY-MM-DD): ")
    enddate = input("Ending date (YYYY-MM-DD): ")
    #pages = int(input("Number of posts: "))

    minyear = re.findall(r'\d{4}', startdate)[0]
    minmonth = re.findall(r'\d{2}', startdate)[2]
    minday = re.findall(r'\d{2}', startdate)[3]
    startdate = datetime.date(int(minyear), int(minmonth), int(minday))

    maxyear = re.findall(r'\d{4}', enddate)[0]
    maxmonth = re.findall(r'\d{2}', enddate)[2]
    maxday = re.findall(r'\d{2}', enddate)[3]
    enddate = datetime.date(int(maxyear), int(maxmonth), int(maxday))

    directory = "./Processed2Posts/" + blog

    #for p in range(1, pages + 1):
    for filename in os.listdir(directory):

        if filename.endswith(".txt"):

            rawfile = os.path.join(directory, filename)

            with open(rawfile) as myfile:
                fulldata = json.loads(myfile.read())

            # extract year, month from post
            year = re.findall(r'\d{4}', fulldata['dateobj'])[0]
            month = re.findall(r'\d{2}', fulldata['dateobj'])[2]
            day = re.findall(r'\d{2}', fulldata['dateobj'])[3]
            date = datetime.date(int(year), int(month), int(day))

            # extract text from post
            text = fulldata['text']
            for tag in fulldata['tags']:
                text += tag
                text += " "
            
            if date <= enddate and date >= startdate:
                bucket += text
                bucket += " "
            else:
                posts.append(text)

posts.insert(0,bucket)

tf = tfidf(posts, inphrase=1)

best = tf.most_common(0)