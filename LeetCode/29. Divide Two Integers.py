"""
https://leetcode.com/problems/divide-two-integers/
Date: 2017 April 30
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend > 0) is (divisor > 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        # while dividend >= divisor:
        # 	quotient += 1
        # 	dividend -= divisor

        while dividend >= divisor:
        	i = 1
        	while dividend >= divisor*i:
        		dividend -= divisor*i
        		quotient += i
	        	i *= 2
        return max(min(sign * quotient, 2147483647), -2147483648)