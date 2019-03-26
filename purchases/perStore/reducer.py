#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys

# keep track of sales total and key 
salesTotal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # mapper send two values
    thisKey, thisSale = data

    # change line 
    if oldKey and oldKey != thisKey:
      print oldKey, "\t", salesTotal
      
      oldKey = thisKey
      salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

    # process the last key
    if oldKey != None:
      print oldKey, "\t", salesTotal
  # print "{0}\t{1}".format(oldKey, salesTotal)

