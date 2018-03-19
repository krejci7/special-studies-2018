from tfidf3 import tfidf
from tfidf3 import process

# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
# from nltk.tokenize import word_tokenize

sentences = []
#0:
sentences.append("This is a sentence with a certain number of words and a certain length which only mentions dogs one time")
sentences.append("I love dogs so much and dogs are amazing yay beautiful dogs")
sentences.append("I am really just trying to write some test sentences; I don't have too much of a goal here")
sentences.append("I love dogs, you love dogs, who doesn't love dogs? What kind of fool would not recognize that animals of the canine variety are fantastic?")
sentences.append("This is just a very long sentence in which I would like to prove that even if there are a lot of words, it is able to choose only the ten most common which I suppose is a little silly here because most words are only used once but I bet word will win.")
#5:
sentences.append("These sentences are almost literally identical.")
sentences.append("These sentences are not literally identical.")


final = process(sentences)

test = tfidf(final, 100)
print(test.most_common_all(10))
print(test.cos_sim(1,3))
print(test.cos_sim(4,3))
print(test.cos_sim_all()[1,3])
print(test.cos_sim_all()[4,3])






# lem = WordNetLemmatizer()

# def conv(pos):
#     if pos.startswith('J'):
#         return wordnet.ADJ
#     elif pos.startswith('V'):
#         return wordnet.VERB
#     elif pos.startswith('R'):
#         return wordnet.ADV
#     else:
#         return wordnet.NOUN

# def tokenize(str):
#     return word_tokenize(str)

# def tag(list):
#     return nltk.pos_tag(list)

# tagged = []
# for s in sentences:
#     tagged.append(tag(tokenize(s)))

# final = {}

# lemmatize
# for t in tagged:
#     index = tagged.index(t)
#     string = ""
#     for i in t:
#         string += lem.lemmatize(i[0],conv(i[1]))
#         string += " "
#     final[index] = string