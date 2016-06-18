#!/usr/bin/env python
# coding:utf-8

from collections import defaultdict
from math import log

totalDoc_train = 0
reader = open("./totalDoc_train","r")
for line in reader:
   totalDoc_train = float(line)
reader.close()

counter = 0
vocabHash = defaultdict(int)
idfArray = []
reader_TermList = open("./TermList","r")
for line in reader_TermList:
  data = line.strip().split('\t')
  index = data[0] + "::" + data[1]
  #vocabHash[Type::vocablary]=wordIndex(1~number of vocab)
  vocabHash[index] = counter
  idfArray.append(log(totalDoc_train/float(data[2])))
  counter = counter + 1
reader_TermList.close()

writer_trainListFile = open("./trainList","w")
writer_testListFile = open("./testList","w")
writer_trainDatFile = open("./train.dat","w")
writer_testDatFile = open("./test.dat","w")
reader_trainFiles = open("./trainFiles","r")
reader_testFiles = open("./testFiles","r")
for trainFile in reader_trainFiles:
  print "Processing Train:"+trainFile.strip()
  writer_trainListFile.write(trainFile.strip()+"\n")
  docInfo = {}
  # process every File
  reader_textFile = open(trainFile.strip(),"r")
  for line in reader_textFile:
    # process every Word
    data = line.strip().split('\t')
    if vocabHash.has_key(data[0]+"::"+data[1]):
      #docInfo[wordIndex]=TFIDFvalue
      docInfo[vocabHash[data[0]+"::"+data[1]]] = data[2]
  reader_textFile.close()
  if len(docInfo)>0:
    string = str(len(docInfo))
    for k,v in sorted(docInfo.items()):
      value = float(v) * float(idfArray[k])
      string += " %s:%s" % (str(k),str(value))
    writer_trainDatFile.write(string+"\n")

for testFile in reader_testFiles:
  print "Processing Test:"+testFile.strip()
  writer_testListFile.write(testFile.strip()+"\n")
  docInfo = {}
  # proces every File
  reader_textFile = open(testFile.strip(),"r")
  for line in reader_textFile:
    #process every Word
    data = line.strip().split('\t')
    if vocabHash.has_key(data[0]+"::"+data[1]):
      docInfo[vocabHash[data[0]+"::"+data[1]]] = data[2]
  reader_textFile.close()
  if len(docInfo) > 0:
    string = str(len(docInfo))
    for k,v in sorted(docInfo.items()):
      value = float(v) * float(idfArray[k])
      string += " %s:%s" % (str(k),str(value))
    writer_testDatFile.write(string+"\n")
    
reader_trainFiles.close()
reader_testFiles.close()
writer_trainDatFile.close()
writer_testDatFile.close()
writer_trainListFile.close()
writer_testListFile.close()
