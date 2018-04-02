import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import json
import string

blog = input("Blog name: ")
pages = int(input("Number of posts: "))

for x in range(1, pages + 1):

    rawfile = "RawPosts/" + blog + "/" + str(x) + ".txt"
    procfile = "Processed2Posts/" + blog + "/" + str(x) + ".txt"

    with open(rawfile) as myfile:
        fulldata = json.loads(myfile.read())

    data = fulldata['text']

    file = open(procfile, "w")

    lem = WordNetLemmatizer()
    translator=str.maketrans('','',string.punctuation)

    def conv(pos):
        if pos.startswith('J'):
            return wordnet.ADJ
        elif pos.startswith('V'):
            return wordnet.VERB
        elif pos.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    tokenized = word_tokenize(data)
    tagged = nltk.pos_tag(tokenized)
    
    stringx = ""
    for i in tagged:
        stringx += lem.lemmatize(i[0],conv(i[1]))
        stringx += " "
    stringx = stringx.translate(translator)

    fulldata['text'] = stringx

    file.write(json.dumps(fulldata))

file.close()