from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
from itertools import islice
from numpy import nditer
import matplotlib.pyplot as plt

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import string

# from itertools recipes
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


class tfidf:

    # dictionary = appropriately processed dictionary of document names and their contents
    def __init__(self, dictionary, maxfeatures=2000, inphrase=2, vocab=None):
        self.maxf = maxfeatures
        self.dict = dictionary
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=maxfeatures, analyzer='word', ngram_range=(1,inphrase),
                vocabulary=vocab)
        self.tfs = self.vectorizer.fit_transform(self.dict.values())
        self.names = self.vectorizer.get_feature_names()

    def most_common(self, document, n=10):
        dense = self.tfs.todense()
        # termfreq = [(term1, frequency1), (term2,frequency2), ...]
        termfreq = []
        for j in range(0, len(self.names)):
            if (dense[document,j] > 0):
                termfreq.append((j, dense[document,j]))
        
        # print 10 most common words for one document
        sort = sorted(termfreq, key=lambda x: x[1], reverse=True)
        best = take(n, sort)
        print("DOCUMENT %d" % document)
        for y in best:
            print('{0: <20} {1}'.format(self.names[y[0]], y[1]))
        return best

    # print n most common words across all documents
    def most_common_all(self, n=10):
        tfidfsmall = TfidfVectorizer(stop_words='english', max_features=n)
        tfssmall = tfidfsmall.fit_transform(self.dict.values())
        return tfidfsmall.get_feature_names()

    def cos_sim(self, doc1_name, doc2_name):
        vectorizer = TfidfVectorizer(stop_words='english', max_features=self.maxf)
        sim = vectorizer.fit_transform([self.dict[doc1_name], self.dict[doc2_name]])
        return (sim * sim.T)[0,1]

    def cos_sim_all(self):
        return (self.tfs * self.tfs.T).A
    
    def heat_map(self):
        a = (self.tfs * self.tfs.T).A
        plt.imshow(a, cmap='hot', interpolation='nearest')
        plt.show()
    
    def most_similar(self):
        cossim = (self.tfs * self.tfs.T).A
        it = nditer(cossim, flags=['multi_index'])
        maxval = 0.0
        pair = (0,1)
        while not it.finished:
            index = it.multi_index
            if not (index[0] == index[1]):
                if it[0] > maxval:
                    maxval = it[0]
                    pair = index
            it.iternext()
        return (maxval, pair)

    def least_similar(self):
        cossim = (self.tfs * self.tfs.T).A
        it = nditer(cossim, flags=['multi_index'])
        minval = 1.0
        pair = (0,1)
        while not it.finished:
            index = it.multi_index
            if not (index[0] == index[1]):
                if it[0] < minval:
                    minval = it[0]
                    pair = index
            it.iternext()
        return (minval, pair)
    
    def total_words(self):
        all_words = []
        for x in self.dict.values():
            y = word_tokenize(x)
            for z in y:
                all_words.append(z)
        return len(all_words)


def process(doc_list):
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

    tagged = []
    for s in doc_list:
        tagged.append(nltk.pos_tag(word_tokenize(s)))

    final = {}

    for t in tagged:
        index = tagged.index(t)
        stringx = ""
        for i in t:
            stringx += lem.lemmatize(i[0],conv(i[1]))
            stringx += " "
        stringx = stringx.translate(translator)
        final[index] = stringx

    return final

# def process(docs):
#     lem = WordNetLemmatizer()
#     translator=str.maketrans('','',string.punctuation)

#     def conv(pos):
#         if pos.startswith('J'):
#             return wordnet.ADJ
#         elif pos.startswith('V'):
#             return wordnet.VERB
#         elif pos.startswith('R'):
#             return wordnet.ADV
#         else:
#             return wordnet.NOUN

#     tagged = {}
#     for s in docs.keys():
#         tagged[s] = nltk.pos_tag(word_tokenize(docs[s]))

#     final = {}

#     for t in tagged.keys():
#         stringx = ""
#         for i in tagged[t]:
#             stringx += lem.lemmatize(i[0],conv(i[1]))
#             stringx += " "
#         stringx = stringx.translate(translator)
#         final[t] = stringx

#     return final