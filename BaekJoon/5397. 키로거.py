tc = int(input())
for _ in range(tc):
    log = input()
    left_stack = []
    right_stack = []
    for char in log:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)
        # print(char, left_stack, list(reversed(right_stack)))
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

