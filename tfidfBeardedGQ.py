from tfidf3 import tfidf
from tfidf3 import process
import os
import json

posts = []

directory = "./RawPosts/BeardedGQ"

for filename in os.listdir(directory):

    if filename.endswith(".txt"):

        rawfile = os.path.join(directory, filename)

        with open(rawfile) as myfile:
            fulldata = json.loads(myfile.read())
        
        posts.append(fulldata['text'])

final = process(posts)

tf = tfidf(final, 1000)
print(tf.most_common_all(10))
print(tf.cos_sim(1,3))
print(tf.cos_sim(8,24))
print(tf.cos_sim(9,15))
print(tf.cos_sim(43,31))
print(tf.cos_sim(37,38))