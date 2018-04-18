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


plt.figure(1)
freq = {}

# get blog name and number of posts for each blog
directory = "./Processed2Posts/"

for blog in os.listdir(directory):
    if not blog.startswith("."):
        directory = "./Processed2Posts/" + blog

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

                # freq = {day : number of posts from that day}

                for single_date in (date + timedelta(days = n) for n in range(-window,window + 1)):
                    if single_date in freq:
                        freq[single_date] += 1
                    else:
                        freq[single_date] = 1


x = list(i for i in sorted(freq.keys()))
y = list(freq[i] for i in sorted(freq.keys()))

plt.plot(x,y)
plt.xticks(rotation=90)

plt.show()



# jupyter
# pip3 install jupyter


# could smooth curves if you want
# if you see anomalies, see what they were talking about
# could even TF-IDF on different buckets instead of just looking with your eyes (look at top 5 works that describe the peak)

# overlay posts over time for specific words (top 5 most common)