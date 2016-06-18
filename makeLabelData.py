#!/usr/bin/env python
# coding:utf-8

from collections import defaultdict
import re

reader_fileInfo = open("/home/data/facet/fileInfo","r")
typeHash = {}
for line in reader_fileInfo:
  data = line.split('\t')
  fn = data[0].replace('http://headlines.yahoo.co.jp/hl?a=','')
  matchOB = re.search("::",data[1])
  if matchOB:
    # typeHash[filename] = type
    typeHash[fn] = data[1].split("::")[1]
reader_fileInfo.close()

reader_trainList = open("./trainList","r")
writer_trainLabel = open("./trainLabel","w")
for line in reader_trainList:
  fn = line.strip().split("/")[-1]
  if typeHash.has_key(fn):
    writer_trainLabel.write("%s\t%s\n" % (fn,typeHash[fn]))
  else:
    print "No info in train\n"
reader_trainList.close()
writer_trainLabel.close()

reader_testList = open("./testList","r")
writer_testLabel = open("./testLabel","w")
for line in reader_testList:
  fn = line.strip().split("/")[-1]
  if typeHash.has_key(fn):
    writer_testLabel.write("%s\t%s\n" % (fn,typeHash[fn]))
  else:
    print "No info in test\n"
reader_testList.close()
writer_testLabel.close()
