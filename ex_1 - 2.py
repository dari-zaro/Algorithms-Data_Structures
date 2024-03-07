from collections import deque

size_n = deque(map(int, input().split(' ')))
ochered = deque([0 for i in range(size_n[0])])
for i in range(size_n[1]):
    a_d = input().split(' ')
    a = int(a_d[0])
    d = int(a_d[1])
    if ochered[0] <= a:
        print(a) if ochered[-1] <= a else print(ochered[-1])
        ochered.append(ochered[-1] + d)
        ochered.popleft()
    else:
        print(-1)
