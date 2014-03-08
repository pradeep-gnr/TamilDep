import sys
import os
#import ipdb
import re
import ipdb
import copy
import cPickle
import string
import traceback

ipDir = sys.argv[1]
l = int(sys.argv[2])
conllFile = open(sys.argv[3],"wb")

oldDict = cPickle.load(open(sys.argv[4],"rb")) # Load the Old Pickle !!

# Set up Punctuation Regex !
puncList = list(set(string.punctuation))
pList = map(lambda x: "\%s" %(x) , puncList)
puncRe = re.compile("|".join(pList))

def getLineParts(eachLine):
    parts = eachLine.split()
    return parts

def checkPunc(symbol):
    # Regex to check for a Symbol 
    if puncRe.findall(symbol):
        return True
    return False

def getNewMappingDict(oldDict):
    """
    Removes Punctuations and Makes a new Dict !
    """            
    lenTok = len(oldDict.keys())    
    oldNewMapping ={}
    newOldMapping = {}
    tmpProcessList = []
    tmpProcessList.append(["TEMP"]) # To begin indexing from 1

    # Create a List to work with First !!   
    for i in range(1,lenTok+1):
        # Add each element to the list
        tmpProcessList.append([i,oldDict[i]])

    tmpCopyList = copy.deepcopy(tmpProcessList)
    
    for i in range(1,lenTok+1):
        # Check if each element is a Punctuation !!
        curElement = tmpProcessList[i]
        if checkPunc(curElement[1][0]):
            # Set the tmpFlag in the other last to indicate that you have found a Punctuation !!
            tmpCopyList[i][0] = "PUNC"

            # Decrease the remaining counts !
            j=i+1
            while j<=lenTok:
                tmpCopyList[j][0]=tmpCopyList[j][0]-1
                j=j+1

    # Walk through the two Lists and build Mapping !!           
    for i in range(1,lenTok+1):
        newMapping = tmpProcessList[i][0]
        oldMapping = tmpCopyList[i][0]

        if oldMapping!="PUNC":
            newOldMapping[newMapping] = oldMapping
            oldNewMapping[oldMapping] = newMapping    

    return oldNewMapping,newOldMapping

def getCurFileDetails(curFile, postID):    
    """
    Parsing InfraStructure to parse the file !!
    """    
    curFileDict = {}    
    print curFile
    tFlag=False
    for eachLine in curFile:      
        eachLine=eachLine.strip()  
        chkStr = 'id="1"'
        if chkStr in eachLine:
            tFlag = True
            curID = 1
            allTokens = []
            continue
        
        if tFlag:
            # Process each Line !!
            if eachLine=="</Sentence>":
                oldNewMapping,newOldMapping = getNewMappingDict(curFileDict)
                return curFileDict,oldNewMapping,newOldMapping

            
            parts = getLineParts(eachLine)
            if not parts:
                continue

            if re.findall("\d+\.\d+",parts[0]):
                # Matches a Token !!
                word = parts[1]
                pos = parts[2]
                morph = parts[3] # Other things to add later !!
                curFileDict[curID] = (word,pos)
                curID+=1                   

def getNewHead(curFile,curW,oldNewMapping,newOldMapping,fId):
    """
    Return the new Head !!
    """                
    try:
        oldW = newOldMapping[curW]
        oldHead = oldDict[fId][oldW][1]
        oldHead = int(oldHead)
        if oldHead==0:
            newHead=0
        else:
            newHead = oldNewMapping[oldHead]
        return newHead   
    except:
        traceback.format_exc()
    

def writeToConll(curFileDict,oldNewMapping,newOldMapping,postId):
    """
    Write everything to a CONLL File Format !!
    """                
    lenW = len(curFileDict.keys())
    for i in range(1,lenW+1):
        # Write each word to the File !!
        num = i
        form = curFileDict[i][0]        
        form = str(form)
        form = form.strip()
        lemma = "_"
        pos = curFileDict[i][1]
        features = "_"

        # Get the head 
        head = "1" # DEfault for now !!
        if checkPunc(form):
            head = "_"
        else:
            head = getNewHead(curFileDict,i,oldNewMapping,newOldMapping,postId)        
        
        head = str(head)      

        if head=='None':
            head = getNewHead(curFileDict,i,oldNewMapping,newOldMapping,postId)        
        
        depREL ="_"
        Phead = "_"
        pdepRel = "_"

        allItems = [num,form,lemma,pos,pos,features,head,depREL,Phead,pdepRel]
        allItems = map(lambda x:str(x), allItems)
        conllString = "\t".join(allItems)
        conllFile.write(conllString+"\n")        


for fInd in range(1,l+1):
    curPath = ipDir+os.sep+"%s.op" %(str(fInd))
    curFile = open(curPath,"rb")
    print curFile    

    curFileDict,oldNewMapping,newOldMapping = getCurFileDetails(curFile,fInd)
    # Map details later !
    writeToConll(curFileDict,oldNewMapping,newOldMapping,fInd)
    conllFile.write("\n")

    



