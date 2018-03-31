class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        d = {}
        def recurse(A, B, prev_a, prev_b):
            if not A:
                return 0
            A = A[:]
            B = B[:]
            l = len(A)
            a = A.pop(0)
            b = B.pop(0)
            got = d.get((tuple(A),tuple(B),a,b), [])
            if got:
                norm = got[0]
                rev = got[1]
            else:
                norm = recurse(A,B,a,b)
                rev = recurse(A,B,b,a)
                d[(tuple(A),tuple(B),a,b)] = [norm, rev]
            condition = 6 <= l and l <= 10
            # condition = False
            if condition:
                print("{0}\t{7} {1} {2}\n\t{8} {3} {4}".format(l, a, A, b, B, norm, rev, prev_a, prev_b))
            if not (prev_a < a and prev_b < b):
                whichif = "not (prev_a < a and prev_b < b)"
                # rev = recurse(A, B, b, a)
                res = min(rev, l-rev) + 1
            elif a==b:
                whichif = "a==b"
                # norm = recurse(A,B,a,b)
                res = norm
            elif a!=b:
                whichif = "a!=b"
                # norm = recurse(A,B,a,b)
                # rev = recurse(A,B,b,a)
                if prev_a < b and prev_b < a:
                    res = min(norm, min(rev, l-rev) + 1)
                else:
                    res = norm
            if condition:
                print("\t{}\tnorm:{} rev:{}\tres:{}".format(whichif,norm,rev, res))
            return res
            
        
        res = recurse(A, B, -1, -1)
        return res