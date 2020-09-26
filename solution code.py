try:
    def change(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list
    test=input()
    test=int(test)
    tser=0
    for tser in range(test):
        N, Q = map(int, input().split(" "))
        l = list(map(int, input().split(" ")))
        unsor = 0
        l=[0]+l
        #print(l)
        i=1
        while i<=N:
            if (l[i] != i):
                unsor += 1
            i+=1
        #print(unsor)
        if unsor==0:                 
            print(0)
            continue
        if (all(l[i] >= l[i + 1] for i in range(len(l) - 1))):
            if(N%4!=0 or N%4!=1):
                print("-1")
            else:
                Q = 1
                p = N
                la = 0
                print(N // 2)
                for i in range(0, N // 2):
                    print(p, Q, p - 1)
                    la += 1
                    if (la == 2):
                        la = 0
                        p = p - 2
                    Q += 1
        else:
                ran = 0           
                p_p = 0    
                fin = []            
                i = 0               
                while (i < N + 1):
                    th = i
                    se = l[i]
                    if i == l[l[i]]:
                        i += 1
                        continue
                    else:
                        fir = l[l[i]]
                        change(l, th, se)
                        change(l, th, fir)
                        if (l[se] == se):
                            unsor -= 1
                        if (l[fir] == fir):
                            unsor -= 1
                        if (l[th] == th):
                            unsor -= 1
                        ran += 1
                        fin.append(th)
                        fin.append(se)
                        fin.append(fir)
                    if ran > Q:
                        p_p = -1
                        break
                i = 1
                while (i):                      
                    if unsor > 0 and unsor <= 2:
                        p_p = -1        
                        break
                    else:
                        th = i
                        se = l[i]
                        if th != se:
                            for j in range(i, N + 1):
                                if (j != l[j] and j != th and j != se):
                                    fir = j
                                    change(l,th, se)
                                    change(l,th, fir)
                                    ran += 1
                                    if (l[fir] == fir):
                                        unsor -= 1
                                    if (l[th] == th):
                                        unsor -= 1
                                    if (l[se] == se):
                                        unsor -= 1
                                    fin.append(th)
                                    fin.append(se)
                                    fin.append(fir)
                                    break
                        if i == l[i]:
                            if i != N:
                               i+=1
                            else:
                                break
                        if ran > Q:
                            p_p = -1
                            break
                if unsor == 0 and p_p != -1 and ran <= Q:
                    p_p = ran
                if p_p != -1:
                    print(ran)
                    for i in range(0, len(fin), 3):
                        print(fin[i], fin[i + 1], fin[i + 2])
                else:
                    print(-1)
                    continue
except:
    pass
