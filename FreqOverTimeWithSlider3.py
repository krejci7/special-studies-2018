import nltk
import json
import re
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
from datetime import timedelta
import time
import os
import numpy as np

# size of sliding window
window = 75

# get number of blogs, overlayed or not
numblogs = 1
overlay = 1
freq = {}
x = {}
y = {}

# get blog name and number of posts for each blog
for currblog in range (1, numblogs + 1):
    blog = input("Blog #" + str(currblog) +" name: ")
    #pages = int(input("Number of posts: "))

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

            for single_date in (date + timedelta(days = n) for n in range(-window,window + 1)):
                thisdate = time.mktime(single_date.timetuple())
                if thisdate in freq[currblog]:
                    freq[currblog][thisdate] += 1
                else:
                    freq[currblog][thisdate] = 1
    
    x[currblog] = list(i for i in sorted(freq[currblog].keys()))
    y[currblog] = list(freq[currblog][i] for i in sorted(freq[currblog].keys()))

    trace = go.Scatter(x=x[currblog], y=y[currblog])
    data = [trace]

    tickvs = []
    tickt = []

    for d in np.arange(min(x[currblog]), max(x[currblog])+1.0, 2628000.0): # step = 1 month in seconds (approximately)
        d2 = datetime.datetime.fromtimestamp(d)
        d3 = datetime.date(d2.year, d2.month, d2.day)
        tickvs.append(d)
        tickt.append(d3)

    layout = dict(
        title=blog,
        xaxis=dict(
            tickvals=tickvs,
            ticktext=tickt,
            tickangle = 90
            # rangeslider=dict()
        ),
        yaxis=dict(
            fixedrange = True
        )
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig)


# could smooth curves if you want
# if you see anomalies, see what they were talking about
# could even TF-IDF on different buckets instead of just looking with your eyes (look at top 5 works that describe the peak)

# overlay posts over time for specific words (top 5 most common)