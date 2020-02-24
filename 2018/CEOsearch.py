t = int(input())
for m in range(1,t+1):
    l = int(input())
    exps = []
    nums = []
    for n in range(l):
        ne = input().split()
        n = int(ne[0])
        e = int(ne[1])
        nums.append(n)
        exps.append(e)
    minExp = exps[-1]+1
    numLeft = 0
    dif = 0
    for i in range(len(nums)-1, 0, -1):
        dif += nums[i] * exps[i] - nums[i-1]
        if (dif)<0:
            numLeft+=dif
            dif = 0
    numLeft = abs(numLeft) + nums[-1]
    res = max(minExp, numLeft)
    print('Case #{}: {}'.format(m, res))