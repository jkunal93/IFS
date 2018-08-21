# Find Adjectives
import nltk

sentence =  raw_input("What are you Looking for:")

tk = sentence.split()
tagged = nltk.pos_tag(tk)
adjectives = [adj for adj,pos in tagged \
    if (pos == 'JJ')]
print adjectives
