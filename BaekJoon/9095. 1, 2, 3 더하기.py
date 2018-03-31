#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: 9095. 1, 2, 3 더하기.py
# @Created:   2018-03-31 22:38:59  seo (simon.seo@nyu.edu) 
# @Updated:   2018-03-31 22:52:32  Simon Seo (simon.seo@nyu.edu)
import sys

d = [0,1,2,4]
def f(N):
    if N < len(d):
        return d[N]
    for i in range(len(d),N+1): #4~N
        d.append(d[i-3] + d[i-2] + d[i-1])
    return d[N]

sys.stdin.readline()
for line in sys.stdin:
    print(f(int(line)))


'''정수 4를 1, 2, 3의 조합으로 나타내는 방법은 총 7가지가 있다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
'''