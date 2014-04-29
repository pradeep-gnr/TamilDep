import sys
import os

import sys
import ipdb
import Levenshtein


cFile = open(sys.argv[1],"rb")

# Fist process the conll file and extract sentences 
cFileSentences = [] # Empty list of sentences.
foundSentenceMap={} # Keep track of which sentences have already been found.

sentence=""
for ind,eachLine in enumerate(cFile):
    # Extracte sentence.
    comp = eachLine.split("\t")
    #print comp
    
    if eachLine=="\n":
        cFileSentences.append(sentence)
        sentence=""

    else:
        try:
            token = comp[1]
        except:
            print ind
            print comp
        sentence=sentence+" "+token
    
        
cFileSentences.append(sentence)
print len(cFileSentences)
cLen = cFileSentences

print cFileSentences[32]
print cFileSentences[40]
print cFileSentences[41]

