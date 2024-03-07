import sys
from collections import deque
kolvo = int(sys.stdin.readline())
mas = deque(sys.stdin.readline().split(' '))
kpod = int(sys.stdin.readline())
vhod, vhod_maxs,vihod, vihod_maxs, rez = [],[],[],[],[]
mas.append(0)
mvh, mvih = 0, 0
x, c = 0, 0
for i in range(kpod):
    z = int(mas.popleft())
    vhod.append(z)
    if mvh < z:
        mvh = z

    vhod_maxs.append(mvh)
kolvo -= kpod
while kolvo != -1:
    if x == 0:
        z = vhod.pop()
        vihod.append(z)
        if mvih < z:
            mvih = z
        vihod_maxs.append(mvih)
        c += 1
    elif x == 1:
        vihod.pop()
        z = vihod_maxs.pop()
        rez.append(str(z)) if z > mvh else rez.append(str(mvh))
        och = int(mas.popleft())
        vhod.append(och)
        if mvh < och:
            mvh = och
        vhod_maxs.append(mvh)
        kolvo -= 1
        c -= 1

    if c == kpod:
        x = 1
        mvh = 0
    elif c == 0:
        x = 0
        mvih = 0

print(' '.join(rez))