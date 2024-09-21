M = int(input())

A = []
for i in range(0, 11):
  n = M % 3
  for _ in range(n):
    A.append(i)
  M = M // 3

print(len(A))
print(*A)
