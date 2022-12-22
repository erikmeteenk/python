A = 0
B = 0
C = 0
D = 0
for i in range(3):
    for j in range(1,10):
        D = j
        if int(str(D)+str(C)+str(B)+str(A)) == 4 * int(str(A)+str(B)+str(C)+str(D)):
            continue
        for k in range(1,10):
            C = k
            if int(str(D)+str(C)+str(B)+str(A)) != 4 * int(str(A)+str(B)+str(C)+str(D)):
                continue
                    
            for l in range(1,10):
                B = l
                if int(str(D)+str(C)+str(B)+str(A)) != 4 * int(str(A)+str(B)+str(C)+str(D)):
                    continue
                            
                for m in range(1,10):
                    A = m
                    if int(str(D)+str(C)+str(B)+str(A)) == 4 * int(str(A)+str(B)+str(C)+str(D)):
                        continue

print(str(D)+str(C)+str(B)+str(A))
print(str(A)+str(B)+str(C)+str(D))