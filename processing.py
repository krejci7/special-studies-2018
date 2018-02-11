import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

blog = input("Blog name: ")
pages = int(input("Number of posts: "))

for x in range(1, pages + 1):

    rawfile = "RawPosts/" + blog + "/" + str(x) + ".txt"
    procfile = "ProcessedPosts/" + blog + "/" + str(x) + ".txt"

    with open (rawfile, "r") as myfile:
        data=myfile.readlines()

    file = open(procfile, "w")

    ps = PorterStemmer()

    # stem each string in words, add to list
    def stem(words, list):
        for w in words:
            list.append(ps.stem(w))
    
    # return part of speech analysis of string (str)
    def pos(str):
        return nltk.pos_tag(str)

    for paragraph in data:
        # strip newline symbol, word tokenize
        paragraph.replace('\n', '')
        tokenized = word_tokenize(paragraph)

        # stem input
        '''
        stemmed = []
        stem(tokenized, stemmed)
        print(stemmed)
        '''

        # tokenize input
        '''
        tagged = pos(tokenized)
        print(tagged)
        '''

        # stem input, tokenize stemmed content
        '''
        tagged = pos(stemmed)
        print(tagged)
        '''

        # write stemmed content to file
        '''
        for s in stemmed:
            file.write(s + " ")
        '''

    file.close()