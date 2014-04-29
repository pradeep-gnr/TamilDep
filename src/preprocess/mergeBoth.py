import sys
import ipdb
ipFile = open(sys.argv[1],"rb")
morpFile = open(sys.argv[2],"rb")
opFile = open(sys.argv[3],"wb")

# Fetch sentence wise conll information!
sentMap={}
sentId=1
sentLines = []

for ind,eachLine in enumerate(ipFile):
    
    if eachLine=="\n":
        sentMap[sentId]=sentLines
        sentId+=1
        sentLines=[]

    else:
        sentLines.append(eachLine)


if sentLines:
    sentMap[sentId]=sentLines


# Fetch each sentence from the training file and update sentences.

morphSentMap = {}
sentId=1
sentLines = []

for i,eachLine in enumerate(morpFile):
    if eachLine=="\n":
        morphSentMap[sentId]=sentLines
        sentId+=1
        sentLines=[]

    else:
        sentLines.append(eachLine)

if sentLines:
    morphSentMap[sentId]=sentLines

# ASsert the length of each of the files.
conllKeys = sentMap.keys()
morphKeys = morphSentMap.keys()

print len(conllKeys)
print len(morphKeys)

assert len(conllKeys)==len(morphKeys)

l = len(conllKeys)
# Now merge each of the two files.
for i in range(1,l+1):
    morphSentList = morphSentMap[i]
    conllSentList = sentMap[i]

    print len(morphSentList)," ", len(conllSentList)
    defFeatures = "unk|unk"
    # First build a HashMap of the original set.

    # Build a HashMap.
    morphHashMap={}
    for i,eachSent in enumerate(morphSentList):
        if i==0:
            continue
        comps = eachSent.split()
        token = comps[1]
        try:
            features = comps[4]
            morphHashMap[token] = features
        except:
            pass       


    # for each line in the original Conll File ! Loop through and fill values.
    for eachSent in conllSentList:
        comps = eachSent.split()
        token = comps[1]

        #features = comps[6]
        features = morphHashMap.get(token)
        
        if features:
            # Found features !!
            featureString = ""
            featureList = features.split("=")[1].split(",")

            # Process feature list

            for i,eachF in enumerate(featureList):
                if not eachF:
                    featureList[i]="unk"

            featureString="|".join(featureList)

        else:
            # Do not add features !
            featureString="unk|unk|unk|unk|unk|unk|unk|unk"

        comps[6] = featureString
        conllSent = "\t".join(comps)        

        # Write output for 
        opFile.write(conllSent+"\n")

    opFile.write("\n")


    
    
    
        


