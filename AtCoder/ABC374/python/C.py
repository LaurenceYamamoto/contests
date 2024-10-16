N = int(input())
K = list(map(int, input().split()))
K.sort(reverse=True)

def divide_sequence(N, K):
    result = []
    
    def backtrack(index, A, B):
        if index == N:
            result.append((A[:], B[:]))
            return
        
        A.append(K[index])
        backtrack(index + 1, A, B)
        A.pop()
        
        B.append(K[index])
        backtrack(index + 1, A, B)
        B.pop()
    
    backtrack(0, [], [])
    return result

combinations = divide_sequence(N, K)

tmp = None
for i, (A, B) in enumerate(combinations, 1):
    if tmp is None:
        tmp = max(sum(A), sum(B))
    else:
        tmp = min(tmp, max(sum(A), sum(B)))

print(tmp)