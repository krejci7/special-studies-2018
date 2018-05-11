import nltk
import json
import re
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import os

# size of sliding window
window = 90

# get number of blogs, overlayed or not
numblogs = 2
overlay = 1
freq = {}
x = {}
y = {}
plt.figure(1)
blog = input("Blog name: ")
word = input("Term: ")
words = []
or1 = 0
and1 = 0
match = re.match(r'(\S+) (or (\S+) ?)+', word)
if match:
    or1 = 1
    for each in range(1, len(match.groups())+1, 2):
        words.append(match.group(each))
    if None in words:
        words.remove(None)


# get blog name and number of posts for each blog
for currblog in range (1, numblogs + 1):
    
    freq[currblog] = {}
    directory = "./RawPosts/" + blog

    #for p in range(1, pages + 1):
    for filename in os.listdir(directory):

        if filename.endswith(".txt"):

            rawfile = os.path.join(directory, filename)

            #rawfile = "RawPosts/" + blog + "/" + str(p) + ".txt"

            with open(rawfile) as myfile:
                fulldata = json.loads(myfile.read())

            # extract year, month from post
            year = re.findall(r'\d{4}', fulldata['dateobj'])[0]
            month = re.findall(r'\d{2}', fulldata['dateobj'])[2]
            day = re.findall(r'\d{2}', fulldata['dateobj'])[3]
            date = datetime.date(int(year), int(month), int(day))

            # freq = {day : number of posts from that day}

            text = fulldata['text']
            for t in fulldata['tags']:
                text += " "
                text += t
            text += " "
            text += fulldata['title']

            present = False

            if words and or1:
                for w in words:
                    if w.lower() in text.lower():
                        present = True

            elif word.lower() in text.lower():
                present = True

            if present or currblog == 2:
                if currblog == 1:
                    print(date)
                for single_date in (date + timedelta(days = n) for n in range(-window,window + 1)):
                    if single_date in freq[currblog]:
                        freq[currblog][single_date] += 1
                    else:
                        freq[currblog][single_date] = 1

    x[currblog] = list(i for i in sorted(freq[currblog].keys()))
    y[currblog] = list(freq[currblog][i] for i in sorted(freq[currblog].keys()))

    if not overlay and currblog == 1:
        ax1 = plt.subplot(numblogs, 1, currblog)
    if not overlay and not (currblog == 1):
        plt.subplot(numblogs, 1, currblog, sharex = ax1, sharey = ax1)

    plt.plot(x[currblog],y[currblog])
    plt.xticks(rotation=90)

plt.show()



# automate window size; put it as a parameter so you can change it
# e.g. put the post in its day bucket and the days +2 and -2 away from it
# stop asking for the number of posts in each blog
# he recommends day buckets and play with the window
# jupyter
# pip3 install jupyter




# could smooth curves if you want
# if you see anomalies, see what they were talking about
# could even TF-IDF on different buckets instead of just looking with your eyes (look at top 5 works that describe the peak)

# overlay posts over time for specific words (top 5 most common)