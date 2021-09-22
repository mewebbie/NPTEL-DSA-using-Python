def isprime(m):
    list = []
    for i in range(1,m+1):
        if m%i==0:
            list+=[i]
        if len(list)>2:
            return False
    return True

def primeproduct(m):
    if m<0:
        return False
    for i in range(1,m+1):
        for j in range(m,1,-1):
            if isprime(i) and isprime(j):
                if i*j == m:
                    return True
    return False

def delchar(s,c):
    store = ''
    if len(c)>1:
        return s
    for i in s[:]:
        if i!=c:
            store+=i
    return store
    
def shuffle(list1, list2):
    newList = []
    len1 = len(list1)
    len2 = len(list2)
    n= len2
    if(len1 > len2):
        n = len1
    for i in range(0,n):
        if i<len1:
            newList+=[list1[i]]
        if i<len2:
            newList+=[list2[i]]
    return newList