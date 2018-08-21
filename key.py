import re

#Keyword function
def keyword():
    #print "Inside keyword function"
    words = []
    word = raw_input("Enter the Keyword:")
    words = word.split()

    chunks = []
    curr_chunk = []

    for line in open("Insurance.txt","r"):

        if line.startswith("##") and curr_chunk:

            s="".join(curr_chunk)
            chunks.append(curr_chunk[:])
            curr_chunk = []

        curr_chunk.append(line)

    chunks.append(curr_chunk)

    best=0
    count=0
    oc=0
    #no = 1
    final = ""

    for ch in chunks:
        result=0
        total_count=0
        q = "".join(ch)
        s = q.lower()

        for w in words:
            w = w.lower()
# most important piece of code in the file
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(w), s))
# most impoertant piece of code
            if count>0:
                result=result+1
                total_count = total_count + count
        #print "Count is : ", result

        if best<=result and oc<=total_count:
            if best<result and oc<total_count:
                final = ""
            best = result
            oc = total_count
            final += q


    if oc != 0:
        print final
    else:
        print "---------------\nNo match found\n---------------"
