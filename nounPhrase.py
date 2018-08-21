import nltk
import re
from nltk import word_tokenize
#from nltk.corpus import stopwords
#from nltk.chunk import *

grammar = "NP: {<DT>?<JJ>*<NN>*}"
sentence = raw_input("Type a sentence:")
#sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
tokens=word_tokenize(sentence)
tags=nltk.pos_tag(tokens)
cp = nltk.RegexpParser(grammar)
result = cp.parse(tags)
#stopwords = stopwords.words('english')
#print(result)
#print(type(result))
np = []
#print type(result)
for subtree in result.subtrees(filter = lambda t: t.label()=='NP'):
    #print subtree
    for leaf in subtree:
        print leaf[0],
    print " "
