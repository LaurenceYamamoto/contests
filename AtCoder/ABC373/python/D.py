import queue

n, m = map(int, input().split())
N = [None for _ in range(n)]
Q = queue.Queue()

u, v, w = map(int, input().split())
N[u-1] = 0
N[v-1] = w

for _ in range(m-1):
    u, v, w = map(int, input().split())
    Q.put([u-1, v-1, w])

count = 0

while Q.qsize() > 0:
    if count == Q.qsize():
        item = Q.get()
        N[item[0]] = 0
        N[item[1]] = N[item[0]] + item[2]
        count = 0
    else:
        item = Q.get()
        if N[item[0]] is not None:
           N[item[1]] = N[item[0]] + item[2]
        elif N[item[1]] is not None:
            N[item[0]] = N[item[1]] - item[2]
        else:
            count += 1
            Q.put(item)

for i in range(n):
    if N[i] is None:
        print(str(0), " ", end="")
    else:
        print(str(N[i]), " ", end="")
