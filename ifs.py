import nltk
import string
import unicodedata
from nltk.util import ngrams
from nltk import word_tokenize
from nltk.corpus import wordnet

#IFS function
def IFS():

    chunks = []
    curr_chunk = []
    for line in open("Insurance.txt","r"):

        if line.startswith("##") and curr_chunk:

            s="".join(curr_chunk)
            chunks.append(curr_chunk[:])
            curr_chunk = []

        curr_chunk.append(line)

    chunks.append(curr_chunk)

    scores = []
    sentence =  raw_input("What are you Looking for:")
    #sentence = sentence.translate(None, string.punctuation)
    search = sentence.split()

# Noun Phrases
    grammar = "NP: {<DT>?<JJ>*<NN>*<NNS>*}"
    tokens=word_tokenize(sentence)
    tags=nltk.pos_tag(tokens)
    #print tags
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tags)
    leaves = []
    np = []
    nouns = []
    for subtree in result.subtrees(filter = lambda t: t.label()=='NP'):
        noph = ""

        for leaf in subtree:
            #leaves.append(leaf)
            noph = noph +" "+ leaf[0]
        np.append(noph)

    #print np
    """for n in nouns:
        for s in n:
            print s"""
    tagged = nltk.pos_tag(search)
    nouns = [word for word,pos in tagged \
    	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'JJ')]
    #print nouns

    #Alternate phrase
    synphrase = []

    for phrase in np:
        #print "---"+phrase
        for n in nouns:
            if n in phrase:
                #print n+"---"
                syns = wordnet.synsets(n)
                synwords=[]
                #synwords.append(word)

                for s in syns:
                    l = s.lemmas()
                    for j in l:
                        let=unicodedata.normalize('NFKD', j.name()).encode('ascii','ignore')
                        if let not in synwords and let!=n:
                            #print let
                            synwords.append(let)
                            newph = phrase.replace(n,let)
                            synphrase.append(newph)
                        if len(synwords) == 3:
                            break
                    if len(synwords) == 3:
                        break

                #print synwords
    #print np
    #print synphrase


# Looping through all the FAQs
    for ch in chunks:

        score = 0
        q = "".join(ch)
        #print q
        s1 = q.translate(None, string.punctuation)

        bigrams = ngrams(search,2)
        trigrams = ngrams(search,3)

        for grams in trigrams:
            t = " ".join(grams)
            #print t
            if t.lower() in s1.lower():
                score += 20
                #print score

        """for grams in bigrams:
            t = " ".join(grams)
            #print t
            if t.lower() in s1.lower():
                score += 5
                #print score"""

        # Looking for noun phrases
        for n in np:

            if n.lower() in s1.lower():
                score += 10

        scores.append(score)

    if max(scores)==0:
        for ch in chunks:
            q = "".join(ch)
            s1 = q.translate(None, string.punctuation)
            # Looking for synonyms
            included=[]
            for sph in synphrase:
                if sph.lower() in s1.lower() and sph not in included:
                    score += 10
                    included.append(sph)

            if max(scores)==0:
                print "---------------\nNo match found\n---------------"
                return None

    indices = [i for i, x in enumerate(scores) if x == max(scores)]

    for a in indices:
        print "".join(chunks[a])
        faq = "".join(chunks[a])
