#!/usr/bin/env python
# coding:utf-8

sortedCategory = []
reader_categoryInfo = open("./categoryInfo","r")
for line in reader_categoryInfo:
  sortedCategory.append(line.strip().split("\t")[0])
reader_categoryInfo.close()

counter = 0
while len(sortedCategory) > 0:
  print "trainLabel"+str(counter)
  for includedCategory in sortedCategory:
    print includedCategory
  reader_trainLabel = open("./trainLabel","r")
  reader_testLabel = open("./testLabel","r")
  writer_trainLabelIdx = open("./trainLabel"+str(counter),"w")
  writer_testLabelIdx = open("./testLabel"+str(counter),"w")

  for line in reader_trainLabel:
    if(line.strip().split("\t")[1] in sortedCategory):
      writer_trainLabelIdx.write(line.strip()+"\n")
  for line in reader_testLabel:
    if(line.strip().split("\t")[1] in sortedCategory):
      writer_testLabelIdx.write(line.strip()+"\n")

  counter += 1
  del sortedCategory[0]
  reader_trainLabel.close()
  reader_testLabel.close()
  writer_trainLabelIdx.close()
  writer_testLabelIdx.close()
