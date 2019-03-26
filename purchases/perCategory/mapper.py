#!/usr/bin/python
# --*-- coding:utf-8 --*--

# Sales per Category 
import sys

for line in sys.stdin:
	l = line.strip().split(',')

	if len(l) == 6:
		category = l[2]
		sales = l[3]

	# if category == '':
	# 	category = 'None'
	# if sales == '':
	# 	sales = 'None'
		print '%s\t%s' % (category , sales)