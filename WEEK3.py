def expanding(l):
    prevdiff=0
    for i in range(1,len(l)):
        diff=abs(l[i]-l[i-1])
        if diff <= prevdiff:
            return (False)
        prevdiff = diff
    return (True)
  
def sumsquare(l):
    sumOdd = 0
    sumEven = 0
    for i in range(len(l)):
        if l[i]%2 == 0:
            sumEven+=l[i]**2
        else:
            sumOdd+=l[i]**2
    return [sumOdd,sumEven]
  
def transpose(m):
    inc=0
    newList = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        newList.append(row)
    m = newList
    return m