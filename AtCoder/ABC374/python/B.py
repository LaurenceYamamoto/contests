import sys

S = list(input())
T = list(input())

max_length = max(len(S), len(T))

for i in range(max_length):
    try:
        if S[i] != T[i]:
            print(i+1)
            sys.exit()
    except Exception:
        print(i+1)
        sys.exit()

print(0)
