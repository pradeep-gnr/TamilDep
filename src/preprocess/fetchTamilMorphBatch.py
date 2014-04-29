#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

br = Browser()
#br.open("http://ltrc.iiit.ac.in/analyzer/tamil/")
import ipdb

"""
for f in br.forms():
    form = f
    print f
"""
def parseResponse(resultHtml):
    # Parse the HTML and do something.
    resultList=[]
    soup = BeautifulSoup(resultHtml)            

    #print(soup.prettify())
    for tr in soup.findAll('tr'):
        # Find each tr
        td_list = tr.findAll('td')
        if len(td_list)==4:
            finalTxt=""
            for td in td_list:
                text = td.getText()
                text = re.sub("(&nbsp;)*","",text)
                text = re.sub("(&lt)*","",text)
                text = re.sub("(&gt)*","",text)
                finalTxt=finalTxt+"\t"+text

                #print finalTxt
            resultList.append(finalTxt)

    return resultList

#   Batch version! Read from the file
ipFile = open(sys.argv[1],"rb")
opFile = open(sys.argv[2],"wb")

for eachLine in ipFile:
    br.open("http://ltrc.iiit.ac.in/analyzer/tamil/")    
    br.select_form(nr=0)    
    br.form['input']=eachLine
    br.submit()
    resultList = parseResponse(br.response().read())
    resultList=resultList[0:-3]
    
    print eachLine
    # print relevant stuff
    opFile.write("0 temp\n")
    for each in resultList:
        each=each.strip()
        if not each:
            continue
        each = each.strip()
        comp = each.split()
        #print comp
        tokenId = comp[0]
        token_comp = tokenId.split(".")
        #print each
        if len(token_comp)>1:    
            opFile.write(each.encode("UTF-8")+"\n")

    print "\n"










