N, M = map(int,input().split())
A = [0 for _ in range(M)]
B = ["M" for _ in range(M)]

FLAG = [False for _ in range(N)]

for i in range(M):
    TMP1, TMP2 = input().split()
    A[i] = int(TMP1)
    B[i] = TMP2

for i in range(M):
    if B[i] == "M" and FLAG[(A[i]-1)] == False:
        FLAG[(A[i]-1)] = True
        print("Yes")
    else:
        print("No")
