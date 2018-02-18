import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

sent1 = "This is a sentence with a certain number of words and a certain length which only mentions dogs one time"
sent2 = "I love dogs so much and dogs are amazing yay beautiful dogs"

# lemmatize the sentences
lem = WordNetLemmatizer()

def conv(pos):
    if pos.startswith('J'):
        return wordnet.ADJ
    elif pos.startswith('V'):
        return wordnet.VERB
    elif pos.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

tokenized1 = word_tokenize(sent1)
tokenized2 = word_tokenize(sent2)
tagged1 = nltk.pos_tag(tokenized1)
tagged2 = nltk.pos_tag(tokenized2)

lemmatized1 = ""
lemmatized2 = ""

for i in tagged1:
    lemmatized1 += lem.lemmatize(i[0],conv(i[1]))
    lemmatized1 += " "

for i in tagged2:
    lemmatized2 += lem.lemmatize(i[0],conv(i[1]))
    lemmatized2 += " "

# calculate term frequency for each word in each sentence (# of times term mentioned / # number of words in sentence)
tf1 = {}
tf2 = {}
tftotal = {}

words1 = word_tokenize(lemmatized1)
words2 = word_tokenize(lemmatized2)

sent1l = len(words1)
sent2l = len(words2)
totall = sent1l + sent2l

for i in words1:
    if i in tf1:
        tf1[i] += 1
    else:
        tf1[i] = 1
    if i in tftotal:
        tftotal[i] += 1
    else:
        tftotal[i] = 1

for i in words2:
    if i in tf2:
        tf2[i] += 1
    else:
        tf2[i] = 1
    if i in tftotal:
        tftotal[i] += 1
    else:
        tftotal[i] = 1

for j in tf1:
    tf1[j] = tf1[j]/sent1l

for j in tf2:
    tf2[j] = tf2[j]/sent2l

for j in tftotal:
    tftotal[j] = tftotal[j]/totall

# calculate TF-IDF
tfidf1 = {}
tfidf2 = {}

for k in tftotal:
    if k in tf1:
        tfidf1[k] = tf1[k] / tftotal[k]
    if k in tf2:
        tfidf2[k] = tf2[k] / tftotal[k]

print(tfidf1)
print(tfidf2)