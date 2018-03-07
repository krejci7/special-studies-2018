import nltk
import json
import re
import matplotlib.pyplot as plt
import datetime

# get number of blogs, overlayed or not
numblogs = int(input("Number of blogs: "))
if numblogs > 1:
    overlay = int(input("Side by side (0) or overlayed (1) comparison? Enter 0 or 1: "))
else:
    overlay = 1
freq = {}
x = {}
y = {}
plt.figure(1)

# get blog name and number of posts for each blog
for currblog in range (1, numblogs + 1):
    blog = input("Blog #" + str(currblog) +" name: ")
    pages = int(input("Number of posts: "))

    freq[currblog] = {}

    for p in range(1, pages + 1):

        rawfile = "RawPosts/" + blog + "/" + str(p) + ".txt"

        with open(rawfile) as myfile:
            fulldata = json.loads(myfile.read())

        # extract year, month from post
        year = re.findall(r'\d{4}', fulldata['dateobj'])[0]
        month = re.findall(r'\d{2}', fulldata['dateobj'])[2]
        date = datetime.date(int(year), int(month), 1)

        # freq = {month : number of posts from that month}
        if date in freq[currblog]:
            freq[currblog][date] += 1
        else:
            freq[currblog][date] = 1

    x[currblog] = list(i for i in sorted(freq[currblog].keys()))
    y[currblog] = list(freq[currblog][i] for i in sorted(freq[currblog].keys()))

    if not overlay and currblog == 1:
        ax1 = plt.subplot(numblogs, 1, currblog)
    if not overlay and not (currblog == 1):
        plt.subplot(numblogs, 1, currblog, sharex = ax1, sharey = ax1)

    plt.plot(x[currblog],y[currblog])
    plt.xticks(rotation=90)

plt.show()