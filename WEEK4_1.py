def f(x,l):
    lret = []
    for i in range(len(l)):
        if l[i][1] == x:
            lret.append(l[i])
    return (lret)
def histogram(l):
    l = sorted(l)
    lotuples = []
    ct_arr = []
    for i in range(len(l)):
        ct = 0
        for j in range(i, len(l)):
            if l[i]==l[j]:
                ct+=1
        if i==0 or l[i]!=l[i-1]:
            lotuples.append((l[i],ct))
            ct_arr.append(ct)
    l = lotuples
    ct_arr = sorted(ct_arr)
    flist = []
    for i in range(len(ct_arr)):
        if i==0 or ct_arr[i]!=ct_arr[i-1]:
            flist+=f(ct_arr[i],l)
    return (flist)