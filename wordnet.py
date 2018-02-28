import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import json
from nltk.corpus import wordnet

# plags = plagiarized source; plag1 = plagiarism from source; plagn = not plagiarism
plags = "In a small town there was a happy princess She owned a boat which she sailed on the ocean Her boat was red"
plag1 = "In a tiny town there was a joyful princess She had a ship that she sailed in the sea Her ship was pink"
plagn = "This is an entirely original sentence All of this content is unique and it should not resemble the other two strings Also it talks about goats because goats are good"

plags_tok = sent_tokenize(plags)
plag1_tok = sent_tokenize(plag1)
plagn_tok = sent_tokenize(plagn)

# not used
def np_chunk(tokenized):
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


# not used
def ner_chunk(tokenized):
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged)
            print(namedEnt)
    except Exception as e:
        print(str(e))


# word for word similarity
def wfwsimilarity(c1, c2):
    words1 = nltk.word_tokenize(c1)
    words2 = nltk.word_tokenize(c2)
    avg = 0
    # loop to end of shortest sentence
    end = min(len(words1), len(words2))
    for i in range(0, end):
        w1 = wordnet.synsets(words1[i])
        w2 = wordnet.synsets(words2[i])
        # find pair of syns of w1 and w2 that have the maximum similarity
        sim = 0
        for j in w1:
            for k in w2:
                currsim = j.wup_similarity(k)
                if currsim:
                    sim = max(currsim, sim)
        avg += sim
    # return average word similarity
    return avg/end

# plags1 = comparison of plagiarized source and plagiarism, should have high similarity
# other two should have low similarity
plags1 = wfwsimilarity(plags, plag1)
plagsn = wfwsimilarity(plags, plagn)
plag1n = wfwsimilarity(plag1, plagn)
print(plags1, plagsn, plag1n)