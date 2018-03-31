#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: 11052. 붕어빵 판매하기.py
# @Created:   2018-03-31 22:56:00  seo (simon.seo@nyu.edu) 
# @Updated:   2018-03-31 23:53:49  Simon Seo (simon.seo@nyu.edu)

import sys

for line in sys.stdin:
	bN = int(line)
	bP = [0] + list(map(int, sys.stdin.readline().split()))
	d = [0]
	for i in range(1,bN+1): #1~bN
		d.append(bP[i])
		for j in range(i//2+1):
			d[i] = max(d[i],d[i-j]+d[j])
	print(d[bN])

# I=input
# I()
# b,*a=[0],
# for s in map(int,I().split()):a=s,*a;b+=max(map(sum,zip(b,a))),
# I(b[-1])

'''
4
1 5 6 7 10 15
1 5 6 10 11 15
'''