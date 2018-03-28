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

# print(final)

tf = tfidf(final)
print(tf.most_common_all(10))

print(tf.most_similar()[0],tf.most_similar()[1])
print(tf.least_similar()[0],tf.least_similar()[1])

tf.most_common(47)
tf.most_common(53)

# print("total words: ", tf.total_words())