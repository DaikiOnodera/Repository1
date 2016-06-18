#!/usr/bin/env python
# coding:utf-8

from sklearn.feature_extraction import DictVectorizer
from collections import defaultdict
import math

files = []
labels = []
dataArray = []
df = defaultdict(int)
totalDF = 0.0
reader_trainLabel = open("./trainLabel0","r")
for filelist in reader_trainLabel:
  data = filelist.strip().split("\t")
  files.append(data[0])
  labels.append(data[1])
  dirn = data[0].split("-")[0]
  reader_txtFile = open("/home/data/Yahoo/vectors/"+dirn+"/"+data[0],"r")
  info = {}
  totalDF += 1
  for line in reader_txtFile:
    #process in one document
    termInfo = line.strip().split("\t")
    term = ":".join(termInfo[0:-1])
    #term => type:vocab
    df[term] += 1
    info[term] =float(termInfo[-1])
    # info => info[type:vocab] = tfidf
  dataArray.append(info)

for term,ddf in df.items():
  print term
  df[term] = math.log(totalDF/df[term])

# one pair (key:term value:tf) in dataArray
for dat in dataArray:
  total = 0
  for term in dat.keys():
    # dat[term] in tfidfValue of term
    dat[term] *= df[term]
    # total is sum of tfidf in one document
    total += dat[term]
  for term in dat.keys():
    dat[term] /= (total * 0.01)

v = DictVectorizer(sparse=True)
X = v.fit_transform(dataArray)
f = open("train0.dict","w")
f.write("\n".join(v.get_feature_names()))
f.close()
