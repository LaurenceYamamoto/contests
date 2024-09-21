N, Q = map(int, input().split())
S = input()
SS = list(S)
count = 0
for i in range(N - 2):
    if SS[i:i+3] == ['A', 'B', 'C']:
        count += 1

for _ in range(Q):
    X, C = input().split()
    X = int(X)
    X -= 1
    # 元の状態のチェック
    if SS[X] == 'A':
      if X < N-2 and SS[X+1] == 'B' and SS[X+2] == 'C':
        count -= 1
    elif SS[X] == 'B':
      if X > 0 and X < N-1 and SS[X-1] == 'A' and SS[X+1] == 'C':
        count -= 1
    elif SS[X] == 'C':
      if X > 1 and SS[X-2] == 'A' and SS[X-1] == 'B':
        count -= 1
    # 後の状態のチェック
    SS[X] = C
    if SS[X] == 'A':
      if X < N-2 and SS[X+1] == 'B' and SS[X+2] == 'C':
        count += 1
    elif SS[X] == 'B':
      if X > 0 and X < N-1 and SS[X-1] == 'A' and SS[X+1] == 'C':
        count += 1
    elif SS[X] == 'C':
      if X > 1 and SS[X-2] == 'A' and SS[X-1] == 'B':
        count += 1
    print(count)
