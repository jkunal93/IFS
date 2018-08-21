import nltk
import unicodedata
#from nltk import word_tokenize
from nltk.corpus import wordnet

# Then, we're going to use the term "program" to find synsets like so:
word = "buy"
syns = wordnet.synsets(word)
synwords=[]
#synwords.append(word)

for s in syns:
	l = s.lemmas()
	for j in l:
		let=unicodedata.normalize('NFKD', j.name()).encode('ascii','ignore')
		if let not in synwords and let!=word:
			#print let
			synwords.append(let)
		if len(synwords) == 3:
			break
	if len(synwords) == 3:
		break

print synwords
