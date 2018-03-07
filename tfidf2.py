import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

sent1 = "This is a sentence with a certain number of words and a certain length which only mentions dogs one time"
sent2 = "I love dogs so much and dogs are amazing yay beautiful dogs"

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

tagged1 = tag(tokenize(sent1))
tagged2 = tag(tokenize(sent2))

lemmed1 = ""
lemmed2 = ""
final = {}

# lemmatize
for i in tagged1:
    lemmed1 += lem.lemmatize(i[0],conv(i[1]))
    lemmed1 += " "
final[0] = lemmed1

for i in tagged2:
    lemmed2 += lem.lemmatize(i[0],conv(i[1]))
    lemmed2 += " "
final[1] = lemmed2

# calculate tfidf
tfidf = TfidfVectorizer(stop_words='english')
tfs = tfidf.fit_transform(final.values())
names = tfidf.get_feature_names()
dense = tfs.todense()

finaldict = {}

# save matrix as a dictionary
# finaldict = { sentence # : [ (name, freq), (name,freq), ... ] }
for i in range(0, 2):
    finaldict[i] = []
    for j in range(0, len(names)):
        if (dense[i,j] > 0):
            finaldict[i].append((j, dense[i,j]))

print("sent1")
for i in finaldict[0]:
    print('{0: <20} {1}'.format(names[i[0]], i[1]))
print("sent2")
for i in finaldict[1]:
    print('{0: <20} {1}'.format(names[i[0]], i[1]))