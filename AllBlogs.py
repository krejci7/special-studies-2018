import os
import json
from tfidf3 import process

posts = []

directory = "./FullBlogs" 
i = 0
indices = {}

for filename in os.listdir(directory):

    if filename.endswith(".txt"):

        rawfile = os.path.join(directory, filename)

        with open(rawfile) as myfile:
            fulldata = myfile.read()
        
        posts.append(fulldata)

        name = filename.split('.')[0]
        indices[name] = i
        i += 1

final = process(posts)

file = open("FullBlogs/AllBlogs.txt", "w")
file.write(json.dumps(final))
file.close()

file = open("FullBlogs/indices.txt", "w")
file.write(json.dumps(indices))
file.close()