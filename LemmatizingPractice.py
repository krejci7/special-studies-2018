import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import json

lem = WordNetLemmatizer()

with open("RawPosts/BeardedGQ/1.txt") as myfile:
    fulldata = json.loads(myfile.read())

text = fulldata['text']

def conv(pos):

    if pos.startswith('J'):
        return wordnet.ADJ
    elif pos.startswith('V'):
        return wordnet.VERB
    elif pos.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

tokenized = word_tokenize(text)
tagged = nltk.pos_tag(tokenized)

lemmatized = ""

for i in tagged:
    lemmatized += lem.lemmatize(i[0],conv(i[1]))
    lemmatized += " "

# print(text)
# print(lemmatized)