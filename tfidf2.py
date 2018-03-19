import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from itertools import islice

sentences = []
sentences.append("This is a sentence with a certain number of words and a certain length which only mentions dogs one time")
sentences.append("I love dogs so much and dogs are amazing yay beautiful dogs")
sentences.append("I am really just trying to write some test sentences; I don't have too much of a goal here")
sentences.append("I love dogs, you love dogs, who doesn't love dogs? What kind of fool would not recognize that animals of the canine variety are fantastic?")
sentences.append("This is just a very long sentence in which I would like to prove that even if there are a lot of words, it is able to choose only the ten most common which I suppose is a little silly here because most words are only used once but I bet word will win.")

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

def tokenize(str):
    return word_tokenize(str)

def tag(list):
    return nltk.pos_tag(list)

# from itertools recipes
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

tagged = []
for s in sentences:
    tagged.append(tag(tokenize(s)))

final = {}

# lemmatize
for t in tagged:
    index = tagged.index(t)
    string = ""
    for i in t:
        string += lem.lemmatize(i[0],conv(i[1]))
        string += " "
    final[index] = string

# calculate tfidf
tfidf = TfidfVectorizer(stop_words='english', max_features=3000)
tfs = tfidf.fit_transform(final.values())
names = tfidf.get_feature_names()
dense = tfs.todense()

finaldict = {}

# save matrix as a dictionary
# finaldict = { sentence # : [ (name, freq), (name,freq), ... ] }
for i in final.keys():
    finaldict[i] = []
    for j in range(0, len(names)):
        if (dense[i,j] > 0):
            finaldict[i].append((j, dense[i,j]))


# print 10 most common words for each document
for i in final.keys():
    print("sentence " + str(i))
    sort = sorted(finaldict[i], key=lambda x: x[1], reverse=True)
    best = take(10, sort)
    for y in best:
        print('{0: <20} {1}'.format(names[y[0]], y[1]))

# #print 10 most common words overall
# tfidfsmall = TfidfVectorizer(stop_words='english', max_features=10)
# tfssmall = tfidfsmall.fit_transform(final.values())
# namessmall = tfidfsmall.get_feature_names()

# for x in namessmall:
#     print(x)