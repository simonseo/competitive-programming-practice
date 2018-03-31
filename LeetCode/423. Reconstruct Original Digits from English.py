"""
https://leetcode.com/problems/reconstruct-original-digits-from-english
Date: 2017 April 30
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cd = {
        	'g' : 0,
        	'u' : 0,
        	'w' : 0,
        	'x' : 0,
        	'z' : 0,
        	'f' : 0,
        	'h' : 0,
        	's' : 0,
        	'o' : 0,
        	'n' : 0,
        }
        keys = cd.keys()
        for c in s:
        	if c in keys:
        		cd[c] += 1

        cd['f'] -= cd['u']
        cd['h'] -= cd['g']
        cd['s'] -= cd['x']
        cd['o'] -= cd['z'] + cd['w'] + cd['u']
        cd['n'] -= cd['o'] + cd['s']

        return '0'*cd['z'] + '1'*cd['o'] + '2'*cd['w'] + '3'*cd['h'] + '4'*cd['u'] + '5'*cd['f'] + '6'*cd['x'] + '7'*cd['s'] + '8'*cd['g'] + '9'*(cd['n']/2)