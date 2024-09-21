N=int(input())
XP=[[0,0] for _ in range(N)]

X=list(map(int,input().split()))
P=list(map(int,input().split()))

X.sort()
P.sort()

S=[0 for _ in range(N)]
S[0]=P[0]
for i in range(1,N):
    S[i]=S[i-1]+P[i]

Q=int(input())

import bisect
for _ in range(Q):
    L, R = map(int, input().split())
    L = bisect.bisect_right(X, L)
    R = bisect.bisect_left(X, R)
    print(S[R-1]-S[L-1])

