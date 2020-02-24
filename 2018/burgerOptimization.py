t = int(input())
for c in range(1,t+1):
    k = int(input())
    ds = [int(x) for x in input().split()]
    ds.sort()
    optimals = [0]*len(ds)
    i=j=0
    k=len(ds) - 1
    while (j<len(ds)):
        optimals[i] = ds[j]
        if j<len(ds)-1:
            j+=1
            optimals[k] = ds[j]
        j+=1
        i+=1
        k-=1
    add = 1 if len(ds)%2 == 0 else 0
    distances = list(range(len(ds)//2)) + list(range(len(ds)//2-add, -1, -1))
    res = 0
    for i in range(len(ds)):
        res+=(distances[i] - optimals[i])*(distances[i] - optimals[i])
    print('Case #{}: {}'.format(c, res))