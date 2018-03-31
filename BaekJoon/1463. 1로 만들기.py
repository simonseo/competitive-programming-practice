#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: 1463. 1로 만들기.py
# @Created:   2018-03-31 20:22:05  seo (simon.seo@nyu.edu) 
# @Updated:   2018-03-31 20:29:39  Simon Seo (simon.seo@nyu.edu)
import sys


x = int(sys.stdin.readline())
dp = [0,0]
for i in range(2, x+1): #from 2 to x
	cost = float('inf')
	if i % 3 == 0:
		cost = min(cost, dp[i//3]+1)
	if i % 2 == 0:
		cost = min(cost, dp[i//2]+1)
	if i > 1:
		cost = min(cost, dp[i-1]+1)
	dp.append(cost)
print(dp[x])



# if __name__ == '__main__':
# 	main()