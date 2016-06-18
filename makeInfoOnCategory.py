#!/usr/bin/env python
# coding:utf-8

from collections import defaultdict
import os.path

for idx in range(0,8):
  # process for each category data
  features = defaultdict(lambda : defaultdict(int))
  
  reader_trainLabel = open("trainLabel"+str(idx),"r")
  writer_trainFiles = open("./trainFiles"+str(idx),"w")
  for line in reader_trainLabel:
    #trainLabel => filename filetype
    fn = line.strip().split("\t")[0]
    dirn = fn.split("-")[0]
    reader_txtfile = open("/home/data/Yahoo/vectors/"+dirn+"/"+fn)
    writer_trainFiles.write("/home/data/Yahoo/vectors/"+dirn+"/"+fn+"\n")
    for line_file in reader_txtfile:
      data = line_file.strip().split("\t")
      features[data[0]][data[1]] += 1
    reader_txtfile.close()
  reader_trainLabel.close()
  writer_trainFiles.close()

  reader_testLabel = open("./testLabel"+str(idx),"r")
  writer_testFiles = open("./testFiles"+str(idx),"w")
  for line in reader_testLabel:
    fn = line.strip().split("\t")[0]
    dirn = fn.split("-")[0]
    writer_testFiles.write("/home/data/Yahoo/vectors/"+dirn+"/"+fn+"\n")
  reader_testLabel.close()
  writer_testFiles.close()

  writer_TermListIdxInfo = open("./TermList"+str(idx)+"Info","w")
  writer_TermListIdx = open("./TermList"+str(idx),"w")
  counter = 0
  for nType in ["LOCATION","ORGANIZATION","PERSON","NOUN"]:
    writer_TermListIdxInfo.write(str(counter)+"\n")
    for vocab in features[nType]:
      if features[nType][vocab] > 2:
        counter += 1
        writer_TermListIdx.write("%s\t%s\t%d\n" % (nType,vocab,features[nType][vocab]))
  writer_TermListIdx.close()
  writer_TermListIdxInfo.close()
