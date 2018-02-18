import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import json

blog = input("Blog name: ")
pages = int(input("Number of posts: "))

for x in range(1, pages + 1):

    rawfile = "RawPosts/" + blog + "/" + str(x) + ".txt"
    procfile = "ProcessedPosts/" + blog + "/" + str(x) + ".txt"

    with open(rawfile) as myfile:
        fulldata = json.loads(myfile.read())

    data = fulldata['text']

    file = open(procfile, "w")

    ps = PorterStemmer()

    # stem each string in words, add to list
    def stem(words, list):
        for w in words:
            list.append(ps.stem(w))
    
    # return part of speech analysis of string (str)
    def pos(str):
        return nltk.pos_tag(str)

    # strip newline symbol, word tokenize
    tokenized = word_tokenize(data)

    # stem input
    stemmed = []
    stem(tokenized, stemmed)
    fulldata['stemmed'] = stemmed

    # tag pos input
    tagged = pos(tokenized)
    fulldata['pos'] = tagged

    # stem input, tag pos stemmed content
    '''
    tagged = pos(stemmed)
    fulldata['posstemmed'] = tagged
    '''

    # write stemmed content to file
    file.write(json.dumps(fulldata))

file.close()