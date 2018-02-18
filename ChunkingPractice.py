import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import json

with open("RawPosts/BeardedGQ/1.txt") as myfile:
    fulldata = json.loads(myfile.read())

text = fulldata['text']

tokenized = sent_tokenize(text)

print(tokenized)


def np_chunk():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = "NP: {<DT>?<RB.?>*<JJ.?>*<NN.?>+}"
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)    

    except Exception as e:
        print(str(e))

def ner_chunk():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged)
            print(namedEnt)
    except Exception as e:
        print(str(e))


ner_chunk()