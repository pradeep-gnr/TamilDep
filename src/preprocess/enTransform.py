# -*- coding: utf-8 -*-
import sys
import os
import ipdb
import re

EN_TAMIL_DICT = {} # Dict to keep track to tamil to English Transliteratiosn !
PHONE_RE = None
PHONE_RE_STR=""
def initializeDict(mapFile):
    """
    Initialize the dict from the input File !
    """
    global PHONE_RE
    global PHONE_RE_STR
    PHONE_RE_STR="" # Regex to match Tamil Letters !!
    
    mapFile = open(mapFile,"rb")
    for each in mapFile:
        k,v = each.split(':')
        k = k.strip()
        v= v.strip()
        k = k.decode('UTF-8')
        EN_TAMIL_DICT[k] = v

    # Set up Regexes !! Decode 
    keys = EN_TAMIL_DICT.keys()
    keys.sort(key=len, reverse=True)
    for each in keys:
        uEach = each            
        PHONE_RE_STR = PHONE_RE_STR + uEach +"|"

    PHONE_RE_STR = PHONE_RE_STR[0:-1]
    PHONE_RE = re.compile(PHONE_RE_STR,re.UNICODE)        

def getTransliteration(tamilSent):
    """
    Transforms a Tamil Sentence into En format !
    Must match 
    """
    Usent  = tamilSent.decode("UTF-8")
    Usent = Usent.strip()
    #ipdb.set_trace()
    matches = PHONE_RE.findall(Usent)
    matches = filter(lambda x: x, matches)

    op_str =""
    for each in matches:
        each = each.strip()
        op_str=op_str+EN_TAMIL_DICT[each]
    return op_str
    
if __name__=="__main__":
    import ipdb
    mapFile = sys.argv[1]
    initializeDict(mapFile)
    #print EN_TAMIL_DICT
    sampleSent = "ரு ரு"   
    print getTransliteration(sampleSent)    

    



    
