import sys
from collections import deque
stek, stek_maximus = deque([]), deque([])
maximus = 0
for i in range(int(input())):
    strok = sys.stdin.readline()
    if 'pop' in strok:
        stek.pop()
        stek_maximus.pop()
        maximus = stek_maximus[-1]
    elif 'max' in strok:
        print(maximus)
    else:
        vhod = int(strok.split(' ')[1])
        stek.append(vhod)
        if maximus < vhod:
            maximus = vhod
        stek_maximus.append(maximus)