ip = input().split(' ')
n = int(ip[0])
k = int(ip[1])
marks = []
for i in range(n):
    marks.append(int(input()))

msum = 0
for i in range(k+1,n):
    cavg = []
    for j in range(i,-1,-1):
        avgx = []
        cavg.append(marks[j])
        if i-j>k:
            avgf = sorted(cavg)
            for x in range(len(avgf)):
                if x>=k:
                    avgx.append(avgf[x])
                elif avgf[x]>0:
                    avgx.append(avgf[x])
            if i==k+1 or sum(avgx)>msum:
                msum = sum(avgx)
                
print(msum)