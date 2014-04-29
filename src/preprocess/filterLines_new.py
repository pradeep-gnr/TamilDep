#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ipdb
import Levenshtein

rawFile = open(sys.argv[1],"rb")
cFile = open(sys.argv[2],"rb")

opFile = open(sys.argv[3],"wb")
tmpLogFile = open("tmpLog.txt","wb")

# Fist process the conll file and extract sentences 
cFileSentences = [] # Empty list of sentences.
foundSentenceMap={} # Keep track of which sentences have already been found.

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

def wordSimilarityRatio(sent_1,sent_2):
    """
    Computes the similarity between two sentence based on the number of common words they
    have.    
    """  
    
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

# Load the other sentences
rawSentences=[]
lim=500
for i,line in enumerate(rawFile):
    line = line.strip()
    rawSentences.append(line)    
    i+=1
    if i==500:
        break
    

# for each in small sentence, find the best match.
for ci,cSent in enumerate(cFileSentences):
    maxRatio=0
    bestInd=0    
    bestSent=""
    for ri,rSent in enumerate(rawSentences):
        ratio= Levenshtein.ratio(cSent,rSent)
        if ratio>maxRatio:
            maxRatio=ratio
            bestSent=rSent
            bestInd=ri
    
    print "SENT 1: %s" %(cSent)
    print "SENT 2: %s" %(bestSent)
    if maxRatio<0.90:
        tmpLogFile.write("SENT 1: %s\n" %(cSent))
        tmpLogFile.write("SENT 2: %s\n" %(bestSent))
        tmpLogFile.write("%s , %s , %s\n" %(maxRatio,ci+1,bestInd+1))
        

    opFile.write(bestSent+"\n")
    
            
        
    
    



    
