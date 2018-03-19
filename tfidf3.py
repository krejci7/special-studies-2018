from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
from itertools import islice

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# from itertools recipes
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


class tfidf:

    # dictionary = appropriately processed dictionary of document names and their contents
    def __init__(self, dictionary, maxfeatures):
        self.maxf = maxfeatures
        self.dict = dictionary
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=maxfeatures)
        self.tfs = self.vectorizer.fit_transform(self.dict.values())
        self.names = self.vectorizer.get_feature_names()

    def most_common(self, document, n):
        dense = self.tfs.todense()
        # termfreq = [(term1, frequency1), (term2,frequency2), ...]
        termfreq = []
        for j in range(0, len(self.names)):
            if (dense[document,j] > 0):
                termfreq.append((j, dense[document,j]))
        
        # print 10 most common words for one document
        sort = sorted(termfreq, key=lambda x: x[1], reverse=True)
        best = take(n, sort)
        for y in best:
            print('{0: <20} {1}'.format(self.names[y[0]], y[1]))
        return best

    # print n most common words across all documents
    def most_common_all(self, n):
        tfidfsmall = TfidfVectorizer(stop_words='english', max_features=n)
        tfssmall = tfidfsmall.fit_transform(self.dict.values())
        return tfidfsmall.get_feature_names()

    def cos_sim(self, doc1_name, doc2_name):
        vectorizer = TfidfVectorizer(stop_words='english', max_features=self.maxf)
        sim = vectorizer.fit_transform([self.dict[doc1_name], self.dict[doc2_name]])
        return (sim * sim.T)[0,1]

    def cos_sim_all(self):
        return (self.tfs * self.tfs.T).A


# lemmatize; returns list of lemmatized documents as strings
def process(doc_list):
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

    tagged = []
    for s in doc_list:
        tagged.append(nltk.pos_tag(word_tokenize(s)))

    final = {}

    for t in tagged:
        index = tagged.index(t)
        string = ""
        for i in t:
            string += lem.lemmatize(i[0],conv(i[1]))
            string += " "
        final[index] = string

    return final