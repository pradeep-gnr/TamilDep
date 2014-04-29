import sys
import os
import ipdb

ipFile = open(sys.argv[1],"rb")
opFile = open(sys.argv[2],"wb")

for each in ipFile:
    #
    opFile.write(each+"\n")
