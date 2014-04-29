#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ipdb
import Levenshtein

rawFile = open(sys.argv[1],"rb")
cFile = open(sys.argv[2],"rb")

opFile = open(sys.argv[3],"wb")

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

def printMissingSents():
    """
    Print Missing sentences
    """
    global foundSentenceMap
    keys = foundSentenceMap.keys()
    keys.sort()
    print keys


def checkLinePresent(line,cFileSentences):
    # Check if the line is present int the corpus.
    global foundSentenceMap
    bestSent=""
    maxRatio = 0
    for ind,each_sent in enumerate(cFileSentences):
        ratio =  Levenshtein.ratio(each_sent,line)
        if ratio>maxRatio:
            bestSent = each_sent
            maxRatio = ratio 
            bestInd = ind

    return bestSent,maxRatio,bestInd
    

wCount=0    
for i,line in enumerate(rawFile):

    #print i
    #Proces
    # Match each line with sentence list
    isPresent= False
    [sent,ratio,ind] = checkLinePresent(line,cFileSentences)

    #print "SENT 1 : %s" %(line)
    #print "SENT 2 : %s" %(sent)
    if ratio>0.90:
        print "SENT 1 : %s" %(line)
        print "SENT 2 : %s" %(sent)

        foundSentenceMap[ind]=True
        opFile.write(line)
        wCount+=1        
        print wCount
        printMissingSents()
            
    if wCount==cLen:
        break
        

    



    
