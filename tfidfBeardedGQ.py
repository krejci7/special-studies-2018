from tfidf3 import tfidf
from tfidf3 import process
import os
import json

# dated: transgenders, transsexual, transgendered, male, female, "born male", "born female", natal, sex change, transvestite, tgirl, tgirls,
# transform, transgenderism, "genetic male", "genetic female", protogay, prehomosexual, homosexual
#
# modern: transgender, trans, nonbinary, genderqueer, AMAB, DMAB, AFAB, DFAB, CAMAB, CAFAB, SRS, GRS, "assigned male", "assigned female",
# queer, transition, transitioning, legible, privilege, GNC, "gender nonconforming"
#
vocab = ["transgender", "trans", "nonbinary", "genderqueer", "AMAB", "DMAB", "AFAB", "DFAB", "CAMAB", "CAFAB", "SRS", "GRS", "assign male",
"assign female", "queer", "transition", "legible", "privilege", "GNC", "gender nonconforming","gay","transgenders", "transsexual",
"transgendered","born male","born female","natal","sex change","transvestite","tgirl","tgirls","transform","transgenderism","genetic male",
"genetic female","protogay","prehomosexual","homosexual"]

modern = ["transgender", "trans", "nonbinary", "genderqueer", "AMAB", "DMAB", "AFAB", "DFAB", "CAMAB", "CAFAB", "SRS", "GRS", "assign male",
"assign female", "queer", "transition", "legible", "privilege", "GNC", "gender nonconforming","gay"]

dated = ["transgenders", "transsexual","transgendered","born male","born female","natal","sex change","transvestite","tgirl","tgirls",
"transform","transgenderism","genetic male","genetic female","protogay","prehomosexual","homosexual"]



posts = []

directory = "./RawPosts/BeardedGQ"

for filename in os.listdir(directory):

    if filename.endswith(".txt"):

        rawfile = os.path.join(directory, filename)

        with open(rawfile) as myfile:
            fulldata = json.loads(myfile.read())
        
        posts.append(fulldata['text'])

final = process(posts)

# print(final)

tf = tfidf(final, maxfeatures=2000, vocab=vocab)
# print(tf.most_common_all(10))

# print(tf.most_similar()[0],tf.most_similar()[1])
# print(tf.least_similar()[0],tf.least_similar()[1])

# tf.most_common(47)
# tf.most_common(53)

# print("total words: ", tf.total_words())

mod = {}
dat = {}

modavg = 0
datavg = 0

best = tf.most_common(47,50)

for y in best:
    if tf.names[y[0]] in modern:
        modavg += y[1]
    if tf.names[y[0]] in dated:
        datavg += y[1]
modavg = modavg / len(modern)
datavg = datavg / len(dated)