'''
solve("x-(y+z)") = "x-y-z"
solve("x-(y-z)") = "x-y+z"
solve("u-(v-w-(x+y))-z") = "u-v+w+x+y-z"
solve("x-(-y-z)") = "x+y+z"
There are no spaces in the expression. Only two operators are given: "+" or "-".
'''

def solve(s):
    stack = []
    operator = 0 # 0 if +, 1 if -, but only when opening paranthesis
    res = ""
    for c in s:
        if c=="(":
            stack.append(operator)
        elif c==")":
            stack.pop()
        elif c=="-" or c=="+":
            pass
        else:
            res += "-" if (sum(stack)%2 != operator) else "+" #need to remove + in beginning
            res += c
        operator = 1 if c=="-" else 0
    res = res[1:] if res[0] == "+" else res
    return res