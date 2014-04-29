#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ipdb
import Levenshtein
import string

#rawFile = open(sys.argv[1],"rb")
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

# remove all punctuations from the 
cFileSentences.append(sentence)
newSentences = []
for sentence in cFileSentences:
    sentence_comps=sentence.split()
    sentence_comps[-1] =sentence_comps[-1].strip()
    if sentence_comps[-1]=="0":
        sentence_comps=sentence_comps[0:-1]
        sentence=" ".join(sentence_comps)
        newSentences.append(sentence)
    else:
        newSentences.append(sentence)
        a=1
    


for each in newSentences:
    # Strip punctuation
    each = ' '.join(word.strip(string.punctuation) for word in each.split())
    #replace last word with last_word+space
    each=each.rstrip()
    each=each+"."
    print each
