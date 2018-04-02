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

vocab = ["trans", "nonbinary", "genderqueer", "AMAB", "DMAB", "AFAB", "DFAB", "CAMAB", "CAFAB", "SRS", "GRS", "assign male",
"assign female", "queer", "transition", "legible", "privilege", "GNC", "gender nonconforming","gay","transgenders", "transsexual",
"transgendered","bear male","bear female","natal male", "natal female","sex change","transvestite","tgirl","tgirls","transform",
"transgenderism","genetic male","genetic female","protogay","prehomosexual","homosexual", "become man", "become woman","biological male",
"biological female","NB","enby", "transmasculine","transfeminine", "mutilate","cis","autogynephile","autogynephiles","autogynephilia",
"autogynephilic"]#,"transgender"]

modern = ["trans", "nonbinary", "genderqueer", "AMAB", "DMAB", "AFAB", "DFAB", "CAMAB", "CAFAB", "SRS", "GRS", "assign male",
"assign female", "queer", "transition", "legible", "privilege", "GNC", "gender nonconforming","gay","NB","enby","transmasculine",
"transfeminine","cis"]#, "transgender"]

dated = ["transgenders", "transsexual","transgendered","bear male","bear female","natal male", "natal female","sex change","transvestite",
"tgirl","tgirls", "transform","transgenderism","genetic male","genetic female","protogay","prehomosexual","homosexual","become man",
"become woman","biological male", "biological female", "mutilate","autogynephile","autogynephiles","autogynephilia","autogynephilic"]


numblogs = 1
plt.figure(1)
mod = {}
dat = {}
freq = {}

# get blog name and number of posts for each blog
for currblog in range (1, numblogs + 1):
    blog = input("Blog name: ")
    #pages = int(input("Number of posts: "))

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
            text = {0:fulldata['text']}
            for tag in fulldata['tags']:
                text[0] += tag
                text[0] += " "

            tf = tfidf(text, vocab=vocab, inphrase=2, stopwords=None)

            best = tf.most_common(0,50, False)

            modavg = 0
            datavg = 0
            modnum = 0
            datnum = 0

            for item in best:
                if tf.names[item[0]] in modern:
                    modavg += item[1]
                    modnum += 1
                if tf.names[item[0]] in dated:
                    print(tf.names[item[0]], rawfile)
                    datavg += item[1]
                    datnum += 1
            if modnum:
                modavg = modavg / modnum
            if datnum:
                datavg = datavg / datnum

            # modtot = 0
            # dattot = 0

            # for item in best:
            #     if tf.names[item[0]] in modern:
            #         modtot += 1
            #     if tf.names[item[0]] in dated:
            #         dattot += 1
            # modavg = modtot / len(modern)
            # datavg = dattot / len(dated)

            # print(modavg, datavg)

            # freq = {day : number of posts from that day}

            for single_date in (date + timedelta(days = n) for n in range(-window,window + 1)):
                if single_date in mod:
                    mod[single_date] += modavg
                else:
                    mod[single_date] = modavg
                if single_date in dat:
                    dat[single_date] -= datavg
                else:
                    dat[single_date] = -1 * datavg

            for single_date in (date + timedelta(days = n) for n in range(-window,window + 1)):
                if single_date in freq:
                    freq[single_date] += 1
                else:
                    freq[single_date] = 1
            
    for single_date in mod:
        mod[single_date] = mod[single_date] / freq[single_date]
        if mod[single_date] > 1:
            print("woah", mod[single_date])
    for single_date in dat:
        dat[single_date] = dat[single_date] / freq[single_date]
        if dat[single_date] < -1:
            print("woah", dat[single_date])
    


    x = list(i for i in sorted(dat.keys()))
    y = list(dat[i] for i in sorted(dat.keys()))

    ax1 = plt.subplot(2, 1, 1)

    plt.plot(x,y)
    plt.xticks(rotation=90)

    x = list(i for i in sorted(mod.keys()))
    y = list(mod[i] for i in sorted(mod.keys()))

    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.axhline(0, color='black')

    axes = plt.gca()
    axes.set_ylim([-1.1,1.1])

    x = list(i for i in sorted(freq.keys()))
    y = list(freq[i] for i in sorted(freq.keys()))

    plt.subplot(2, 1, 2, sharex = ax1)

    plt.plot(x,y)
    plt.xticks(rotation=90)

plt.show()



# jupyter
# pip3 install jupyter


# could smooth curves if you want
# if you see anomalies, see what they were talking about
# could even TF-IDF on different buckets instead of just looking with your eyes (look at top 5 works that describe the peak)

# overlay posts over time for specific words (top 5 most common)