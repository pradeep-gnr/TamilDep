import sys
import ipdb

"""
Read a Corpora and print the  output in custom dependency annotation format !!
"""

corpora_file = open(sys.argv[1],"rb")
op_file = open(sys.argv[2],"wb")

for i,each in enumerate(corpora_file):    
    op_file.write("\n\n")
    op_file.write("SENT ID %s : %s\n" %(i+1,each))
    words = each.split()
    
    for j,each_word in enumerate(words):
        op_file.write("\n%s\t%s" %(j+1,each_word))
    

    
    
    
    



