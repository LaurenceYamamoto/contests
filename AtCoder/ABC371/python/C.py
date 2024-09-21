N = int(input())
G = [[False for _ in range(N)] for _ in range(N)]
H = [[False for _ in range(N)] for _ in range(N)]

MG = int(input())
for _ in range(MG):
    u, v = map(int,input().split())
    G[u-1][v-1] = G[v-1][u-1] = True

MH = int(input())
for _ in range(MH):
    a, b = map(int,input().split())
    H[a-1][b-1] = True
    H[b-1][a-1] = True

A = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N-1):
    TMP = list(map(int,input().split()))
    for j in range(len(TMP)):
        A[i][i+j+1] = TMP[j]
for i in range(N):
    for j in range(i):
        A[i][j] = A[j][i]

import itertools
permutations = list(itertools.permutations(range(N)))

cost = 2147483647
for perm in permutations:
    costTmp = 0
    for i in range(N):
      for j in range(i+1, N):
        if G[perm[i]][perm[j]] != H[i][j]:
          costTmp += A[i][j]
    cost = min(cost, costTmp)
  
print(cost)
