S = list(input())
M = {}

for i in range(len(S)):
    M[S[i]] = i


pos = M["A"]
count = 0

for c in range(66, 91):
    c = chr(c)
    count += abs(M[c] - pos)
    pos = M[c]

print(count)
