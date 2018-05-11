import nltk
import random
import os
import json
from nltk.tokenize import word_tokenize
import pickle
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools
import numpy as np

print("loaded imports")

# documents = []

# directory = "./Processed2Posts/"

# for blog in os.listdir(directory):
#     if not blog.startswith("."):

#         path = directory + blog + "/"

#         for filename in os.listdir(path):

#             if filename.endswith(".txt"):

#                 rawfile = os.path.join(path, filename)

#                 with open(rawfile) as myfile:
#                     fulldata = json.loads(myfile.read())
                
#                 text = word_tokenize(fulldata['text'])
                
#                 documents.append((text, blog))

# all_words = []
# for x,y in documents:
#     for w in x:
#         all_words.append(w.lower())

# print("all words assembled")

# all_words = nltk.FreqDist(all_words)

# word_features = list(all_words.keys())

# print("word features assembled")

documents_f = open("documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()
print("loaded documents")

# random.shuffle(documents)

word_features_f = open("word_features.pickle", "rb")
word_features = pickle.load(word_features_f)
word_features_f.close()
print("loaded word_features")

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# featuresets = [(find_features(rev), category) for (rev, category) in documents]

# print("featuresets assembled")

# # set that we'll train our classifier with
# training_set = featuresets[:990]

# # set that we'll test against.
# testing_set = featuresets[990:]

# save_documents= open("documents.pickle","wb")
# pickle.dump(documents, save_documents)
# save_documents.close()

# save_word_features = open("word_features.pickle","wb")
# pickle.dump(word_features, save_word_features)
# save_word_features.close()

# save_training_set = open("training_set.pickle","wb")
# pickle.dump(training_set, save_training_set)
# save_training_set.close()

# save_testing_set = open("testing_set.pickle","wb")
# pickle.dump(testing_set, save_testing_set)
# save_testing_set.close()


# classifier = nltk.NaiveBayesClassifier.train(training_set)


# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

########################### load pickles #################################

training_set_f = open("training_set.pickle", "rb")
training_set = pickle.load(training_set_f)
training_set_f.close()
print("loaded training_set")

testing_set_f = open("testing_set.pickle", "rb")
testing_set = pickle.load(testing_set_f)
testing_set_f.close()
print("loaded testing_set")

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
print("loaded classifier")

##########################################################################


# classifier.show_most_informative_features(15)

# all_words = []
# for x,y in documents:
#     for w in x:
#         all_words.append(w.lower())

# print("all words assembled")

# all_words = nltk.FreqDist(all_words)

# word_features = list(all_words.keys())


# to be used WITHOUT shuffling documents
BeardedGQ = [(find_features(rev), category) for (rev, category) in documents[:22]]
BornWrong = [(find_features(rev), category) for (rev, category) in documents[56:78]]
CFlourish = [(find_features(rev), category) for (rev, category) in documents[81:103]]
DTando = [(find_features(rev), category) for (rev, category) in documents[641:663]]
genderkid = [(find_features(rev), category) for (rev, category) in documents[695:718]]
HerDog = [(find_features(rev), category) for (rev, category) in documents[830:852]]
HMcK = [(find_features(rev), category) for (rev, category) in documents[1027:1049]]
JanitorQ = [(find_features(rev), category) for (rev, category) in documents[1167:1189]]
RadQ = [(find_features(rev), category) for (rev, category) in documents[1407:1429]]
RmyR = [(find_features(rev), category) for (rev, category) in documents[1439:1461]]
TransBlog = [(find_features(rev), category) for (rev, category) in documents[1769:1791]]

featuresets = BeardedGQ + BornWrong + CFlourish + DTando + genderkid + HerDog + HMcK + JanitorQ + RadQ + RmyR + TransBlog

print("featuresets assembled")


# print("testing accuracy")

# print("BeardedGQ: ",(nltk.classify.accuracy(classifier, BeardedGQ))*100)
# print("BornWrong: ",(nltk.classify.accuracy(classifier, BornWrong))*100)
# print("CFlourish: ",(nltk.classify.accuracy(classifier, CFlourish))*100)
# print("DTando: ",(nltk.classify.accuracy(classifier, DTando))*100)
# print("genderkid: ",(nltk.classify.accuracy(classifier, genderkid))*100)
# print("HerDog: ",(nltk.classify.accuracy(classifier, HerDog))*100)
# print("HMcK: ",(nltk.classify.accuracy(classifier, HMcK))*100)
# print("JanitorQ: ",(nltk.classify.accuracy(classifier, JanitorQ))*100)
# print("RadQ: ",(nltk.classify.accuracy(classifier, RadQ))*100)
# print("RmyR: ",(nltk.classify.accuracy(classifier, RmyR))*100)
# print("TransBlog: ",(nltk.classify.accuracy(classifier, TransBlog))*100)



# print("Naive Bayes accuracy: ",(nltk.classify.accuracy(classifier, testing_set))*100)

# mini_set = testing_set[0:50]

names = ["BeardedGQ","BornWrong","CFlourish","DTando","genderkid","HerDog", "HMcK","JanitorQ","RadQ","RmyR","TransBlog"]

mini_set_fts = []
mini_set_ans = []
for each in featuresets:
    mini_set_fts.append(each[0])
    mini_set_ans.append(each[1])

print("set organized")


answers = classifier.classify_many(mini_set_fts)

print("answers determined")

mat = confusion_matrix(answers, mini_set_ans, labels=names)


# from http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')



plt.figure()
plot_confusion_matrix(mat, classes=names, title='Confusion matrix', normalize=True)
plt.show()