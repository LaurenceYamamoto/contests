import itertools

N, S, T = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(N)]

L = list(itertools.permutations(K))

result = None

for P in L:
    tmp1 = [[0 for _ in range(3)] for _ in range(2)] # x, y, time
    tmp2 = [[0 for _ in range(3)] for _ in range(2)] # x, y, time

    for i in range(N):
        drawing_time = (((P[i][2] - P[i][0])**2 + (P[i][3] - P[i][1])**2)**0.5)/T

        #  順序通り
        time1 = drawing_time + tmp1[0][2]
        d = ((tmp1[0][0] - P[i][0])**2 + (tmp1[0][1] - P[i][1])**2)**0.5
        time1 += d/S

        time2 = drawing_time + tmp1[1][2]
        d = ((tmp1[1][0] - P[i][0])**2 + (tmp1[1][1] - P[i][1])**2)**0.5    
        time2 += d/S

        if time1 <= time2:
            tmp2[0] = [P[i][2], P[i][3], time1]
        else:
            tmp2[0] = [P[i][2], P[i][3], time2]

        # 逆順
        time1 = drawing_time + tmp1[0][2]
        d = ((tmp1[0][0] - P[i][2])**2 + (tmp1[0][1] - P[i][3])**2)**0.5
        time1 += d/S

        time2 = drawing_time + tmp1[1][2]
        d = ((tmp1[1][0] - P[i][2])**2 + (tmp1[1][1] - P[i][3])**2)**0.5    
        time2 += d/S

        if time1 <= time2:
            tmp2[1] = [P[i][0], P[i][1], time1]
        else:
            tmp2[1] = [P[i][0], P[i][1], time2]
        
        tmp1 = tmp2
        tmp2 = [[0 for _ in range(3)] for _ in range(2)]
        #print(*tmp1)
    
    if result is None:
        result = min(tmp1[0][2], tmp1[1][2])
    else:
        result = min(result, min(tmp1[0][2], tmp1[1][2]))

print(result)