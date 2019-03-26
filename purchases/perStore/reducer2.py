#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys

salesTotals = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.           
        continue

    store, sale = data
    salesTotals.setdefault(store, 0)
    salesTotals[store] += float(sale)

for store in salesTotals:
    print "{0}\t{1}".format(store, salesTotals[store])

