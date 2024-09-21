# https://atcoder.jp/contests/abc370/tasks/abc370_c
#
# 文字列Sを先頭から探索し、S[i]とT[i]が異なり、かつS[i]がT[i]より辞書順で小さい場合には置き換えていく。
# 次に、文字列Sを末尾から探索し、S[i]とT[i]が異なり、かつS[i]がT[i]より辞書順で小さい場合には置き換えていく。
#
S = list(input())
T = list(input())
L = len(S)

X=[]
tmp=[]
for i in range(L):
    if S[i] != T[i]:
        if S[i] > T[i]:
            S[i] = T[i]
            X.append("".join(S))
        else:
            tmp.append(i)

for i in reversed(tmp):
    S[i] = T[i]
    X.append("".join(S))

print(len(X))
for x in X:
  print(x)
