#!/usr/bin/env python
# coding:utf-8


# from 2015/11/01 trainingData:28days testData:7days
# OUTPUT:
#         dateFile => path of everyTrainingData
#         totalDoc_train => number of train_data
#         totalDoc_test => number of test_data
#         TermList => type,vocabulary,freqCount of everyTrainData

import datetime as dt
import os
from collections import defaultdict

trainDirs = []
testDirs = []
aDate = dt.date(2015,11,1)
for x in range(0,27):
  bDate = aDate + dt.timedelta(days=+x)
  date = bDate.strftime("%Y%m%d")
  trainDirs.append("/home/data/Yahoo/vectors/"+date)
for x in range(28,35):
  bDate = aDate + dt.timedelta(days=+x)
  date = bDate.strftime("%Y%m%d")
  testDirs.append("/home/data/Yahoo/vectors/"+date)

writer_trainFiles = open("./trainFiles","w")
totalDoc_train = 0
features = defaultdict(lambda : defaultdict(int))
for trainDir in trainDirs:
  for trainFile in os.listdir(trainDir):
    totalDoc_train = totalDoc_train + 1
    writer_trainFiles.write ("%s\n" % (trainDir+"/"+trainFile))
    for line in open((trainDir+"/"+trainFile),'r'):
      data = line.strip().split("\t")
      features[data[0]][data[1]] += 1
writer_trainFiles.close()

writer_testFiles = open("./testFiles","w")
totalDoc_test = 0
for testDir in testDirs:
  for testFile in os.listdir(testDir):
    totalDoc_test = totalDoc_test + 1
    writer_testFiles.write("%s\n" % (testDir+"/"+testFile))
writer_testFiles.close()

writer_TrainDocTotal = open("./totalDoc_train","w")
writer_TrainDocTotal.write ("%d" % (totalDoc_train))
writer_TrainDocTotal.close()

writer_TestDocTotal = open("./totalDoc_test","w")
writer_TestDocTotal.write ("%d" % (totalDoc_test))
writer_TestDocTotal.close()

# Construct TermList
writer_TermList = open("./TermList","w")
for x in features:
  for y in features[x]:
    if features[x][y] > 2:
      writer_TermList.write("%s\t%s\t%d\n" % (x,y,features[x][y]))
writer_TermList.close()

counter = 0
for typename in ["LOCATION","ORGANIZATION","PERSON","NOUN"]:
  print counter
  for vocab in features[typename]:
    if features[typename][vocab] > 2:
      counter += 1
