AB, AC, BC = input().split()

AGE = [0, 0, 0]

if AB == ">":
    AGE[0] += 1
else:
    AGE[1] += 1
    
if AC == ">":
    AGE[0] += 1
else:
    AGE[2] += 1
    
if BC == ">":
    AGE[1] += 1
else:
    AGE[2] += 1

AGE2 = sorted(AGE)

if AGE2[1] == AGE[0]:
    print("A")
elif AGE2[1] == AGE[1]:
    print("B")
else:
    print("C")
