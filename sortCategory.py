#!/usr/bin/env python
# coding:utf-8

from collections import defaultdict

categoriesHash = {}
categories = ["スポーツ","エンタメ","国際","国内","経済","地域","IT・科学","ライフ"]
for category in categories:
  categoriesHash[category] = 1

categoryCount = defaultdict(int)
for category in categories:
  reader_trainLabel = open("./trainLabel","r")
  for line in reader_trainLabel:
    if categoriesHash.has_key(line.strip().split("\t")[1]):
      categoryCount[line.strip().split("\t")[1]] += 1
  reader_trainLabel.close()

categoryHash = {}
writer_categoryInfo = open("./categoryInfo","w")
for k,v in sorted(categoryCount.items(), key=lambda x:x[1], reverse=True):
  categoryHash[k] = v
  writer_categoryInfo.write("%s\t%d\n" %(k,v))
writer_categoryInfo.close()
