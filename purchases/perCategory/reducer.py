#!/usr/bin/python
# --*-- coding:utf-8 --*--

# Sales per Category 
import sys

salesTotals = {}

for line in sys.stdin:
	l = line.strip().split(',')

    if len(data) != 2:
        # Something has gone wrong. Skip this line.           
        continue

    store, sale = data