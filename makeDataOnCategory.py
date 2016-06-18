#!/usr/bin/env python
# coding:utf-8

from collections import defaultdict
from math import log

for idx in range(0,8):
  reader_total = open("./totalDoc_train"+str(idx),"r")
  for line in reader_total:
    total = float(line.strip())
  reader_total.close()

  counter = 0
  vocabHash = defaultdict(int)
  idfArray = []
  reader_TermList = open("./TermList"+str(idx),"r")
  for line in reader_TermList:
    data = line.strip().split("\t")
    index = data[0] + "::" + data[1]
    vocabHash[index] = counter
    idfArray.append(log(total/float(data[2])))
    counter += 1
  reader_TermList.close()

  reader_trainFiles = open("./trainFiles"+str(idx),"r")
  writer_trainDatFile = open("./train.dat"+str(idx),"w")
  for trainFile in reader_trainFiles:
    print "Processing Train:"+trainFile.strip()
    docInfo = {}
    reader_textFile = open(trainFile.strip(),"r")
    for line in reader_textFile:
      data = line.strip().split("\t")
      if vocabHash.has_key(data[0]+"::"+data[1]):
        docInfo[vocabHash[data[0]+"::"+data[1]]] = data[2]
    reader_textFile.close()
    if len(docInfo) > 0:
      string = str(len(docInfo))
      for k,v in sorted(docInfo.items()):
        value = float(v) * float(idfArray[k])
        string += " %s:%s" % (str(k),str(value))
      writer_trainDatFile.write(string+"\n")
  reader_trainFiles.close()
  writer_trainDatFile.close()

  reader_testFiles = open("./testFiles"+str(idx),"r")
  writer_testDatFile = open("./test.dat"+str(idx),"w")
  for testFile in reader_testFiles:
    print "Processing Test:"+testFile.strip()
    docInfo = {}
    reader_textFile = open(testFile.strip(),"r")
    for line in reader_textFile:
      data = line.strip().split("\t")
      if vocabHash.has_key(data[0]+"::"+data[1]):
        docInfo[vocabHash[data[0]+"::"+data[1]]] = data[2]
    reader_textFile.close()
    if len(docInfo) > 0:
      string = str(len(docInfo))
      for k,v in sorted(docInfo.items()):
        value = float(v) * float(idfArray[k])
        string += " %s:%s" % (str(k),str(value))
      writer_testDatFile.write(string+"\n")
  reader_testFiles.close()
  writer_testDatFile.close()
