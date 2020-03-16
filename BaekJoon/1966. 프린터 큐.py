
def when_m_printed(n, m):
    priority = list(map(int, input().split()))
    count = 0
    while(True):
        # print(priority, n, m)
        candidate = priority.pop(0)
        if any(p > candidate for p in priority):
            priority.append(candidate)
        else:
            count += 1
            n -= 1
            if m == 0:
                return count
        m = (n + m - 1) % n

test_case_count = int(input())
for _ in range(test_case_count):
    n, m = list(map(int, input().split()))
    print(when_m_printed(n, m))
