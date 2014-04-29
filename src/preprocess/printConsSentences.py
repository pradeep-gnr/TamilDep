#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ipdb
import Levenshtein

rawFile = open(sys.argv[1],"rb")
cFile = open(sys.argv[2],"rb")

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

for i,line in enumerate(rawFile):

    #print i
    #Proces
    # Match each line with sentence list
    print "SENT 1: %s" %(line)
    print "SENT 2: %s" %(cFileSentences[i])
    print "\n"

