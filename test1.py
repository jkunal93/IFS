
"""score=[5,3,4,2,7,4,5,2,2,4,5,7,4,5,2]
high = max(score)
low = min(score)
print high
print low

for i in range(0,len(score)):
	if score[i]==high:
		print i
	if score[i]==low:
		print i"""


# similar words (not working)
"""import nltk
#from nltk.book import *

text = "the quick brown fox jumps over a lazy dog"
test = nltk.Text(text)
#test.similar("two")
print(test.similar("programs"))"""


chunks = []
curr_chunk = []

for line in open("Insurance.txt","r"):

	if line.startswith("##") and curr_chunk:

		s="".join(curr_chunk)
		chunks.append(curr_chunk[:])
		curr_chunk = []

	curr_chunk.append(line)

chunks.append(curr_chunk)
#print "".join(chunks)
for ch in chunks:
	print "".join(ch)
