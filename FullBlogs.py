from tfidf3 import process
import os
import json

blog = "TransBlog"

posts = ""

directory = "./RawPosts/" + blog

for filename in os.listdir(directory):

    if filename.endswith(".txt"):

        rawfile = os.path.join(directory, filename)

        with open(rawfile) as myfile:
            fulldata = json.loads(myfile.read())
        
        posts += fulldata['text'] + " "
        tags = fulldata['tags']
        for x in tags:
            posts += x + " "
        posts += fulldata['title'] + " "


file = open("FullBlogs/" + blog + ".txt","w")
file.write(posts)
file.close()