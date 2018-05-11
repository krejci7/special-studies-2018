import nltk
import json
import re
import plotly.plotly as py
import plotly.graph_objs as go
import datetime
from datetime import timedelta
import os
from tfidf3 import tfidf
from tfidf3 import process

# size of sliding window
window = 30

freq = {}

# get blog name and number of posts for each blog
directory = "./Processed2Posts/"

for blog in os.listdir(directory):
    if not blog.startswith("."):
        directory = "./Processed2Posts/" + blog

        freq[blog] = {}

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
                    if single_date in freq[blog]:
                        freq[blog][single_date] += 1
                    else:
                        freq[blog][single_date] = 1


keys = list(freq.keys())

for blog in keys:
    i = keys.index(blog)
    if i > 0:
        for single_date in freq[keys[i-1]]:
            if single_date in freq[blog]:
                freq[blog][single_date] += freq[keys[i-1]][single_date]
            else:
                freq[blog][single_date] = freq[keys[i-1]][single_date]


for blog in keys:
    i = keys.index(blog)
    if i == 0:
        for single_date in freq['TransBlog']:
            if not (single_date in freq['BeardedGQ']):
                freq['BeardedGQ'][single_date] = 0
    else:
        for single_date in freq['TransBlog']:
            if not (single_date in freq[keys[i]]):
                freq[keys[i]][single_date] = freq[keys[i-1]][single_date]

#x = {}  # list(i for i in sorted(freq.keys()))
#y = {}  # list(freq[i] for i in sorted(freq.keys()))
trace = {}

num = 0
for blog in keys:
    col = 'rbg(' + str(num) + ',2,175)'
    #x[blog] = list(i for i in sorted(freq[blog].keys()))
    #y[blog] = list(freq[blog][i] for i in sorted(freq[blog].keys()))
    trace[blog] = go.Scatter(
        x= list(i for i in sorted(freq[blog].keys())),
        y=list(freq[blog][i] for i in sorted(freq[blog].keys())),
        mode='lines',
        line=dict(width=0.5,
                color=col),
        fill='tonexty',
        name=blog
    )
    num += 23

data = []
for blog in keys:
    data.append(trace[blog])

layout = go.Layout(
    showlegend=True,
    xaxis=dict(
        type='date',
    )
    # yaxis=dict(
    #     type='linear'
    # )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig)

# plt.plot(x,y)
# plt.xticks(rotation=90)

# plt.show()



# jupyter
# pip3 install jupyter


# could smooth curves if you want
# if you see anomalies, see what they were talking about
# could even TF-IDF on different buckets instead of just looking with your eyes (look at top 5 works that describe the peak)

# overlay posts over time for specific words (top 5 most common)