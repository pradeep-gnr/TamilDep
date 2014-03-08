import sys
import os
import ipdb
import cPickle

ip_file = open(sys.argv[1],"rb")

def checkBigLine(line):
    lineComp = line.split()
    if len(lineComp)>=3:
        return True

def getSentParts(line):
    partDict = {}    
    if "SENT" in line:
        return None
    if line == "\n":
        return None        

    try:
        parts = line.split()    
        if not parts:
            return None
        partDict['id'] = parts[0]
        partDict['word'] = parts[1]
        partDict['parent'] = parts[2]
    except:
        print line
        ipdb.set_trace()
    return partDict   
    
if __name__=="__main__":

    cnt = 0
    corpPkl = {}    
    fullSent=""
        
    for eachL in ip_file:
        
        """        
        if "SENT" in eachL:
            if cnt>0:
                corpPkl[cnt]['fullSent']= curSentList
            cnt=cnt+1
            curSentList = []
            continue
        """
        partDict = getSentParts(eachL)        
        if partDict:        
            print eachL
            ID = int(partDict['id']) 
            word = partDict['word']
            parent = partDict['parent'] 

            if ID==1:
                # new Sentence and Word !!
                sentFlag=True
                cnt=cnt+1
                print cnt
                corpPkl[cnt] = {}
                
            corpPkl[cnt][ID] = (word,parent)           
            
    # Write the Pkl to File !
    #ipdb.set_trace()
    cPickle.dump(corpPkl,open(sys.argv[2],"wb"))
                
        
          
        
        
        
