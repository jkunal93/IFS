import nltk
import string
from nltk.corpus import wordnet

"""chunks = []
curr_chunk = []
for line in open("UM.txt","r"):

    if line.startswith("##") and curr_chunk:

        s="".join(curr_chunk)
        chunks.append(curr_chunk[:])
        curr_chunk = []

    curr_chunk.append(line)

chunks.append(curr_chunk)"""
#print chunks[1]
#text = "Hello, this is my para. You're also my Name."
#g = text.split()
top = []
sentence =  raw_input("What are you Looking for:")
tokens = nltk.word_tokenize(sentence)

tk = sentence.split()
tagged = nltk.pos_tag(tk)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)

print joined
print into_string
