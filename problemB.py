
# coding: utf-8

# In[10]:


f = open('B-large-practice.in', 'r')
T = int(f.readline())
out = open("output.txt", "w");


for j in range (T):
    L = int(f.readline());
    NE = []
    for i in range(L):
        splitted = f.readline().split(" ");
        NE.append([int(splitted[0]), int(splitted[1])]);
    leftover = 0;
    NEprod = [x[0]*x[1] for x in NE];
    for i in range(1, L):
        leftover = NEprod[i]-NE[i][0]+leftover;
        if leftover > 0:
            leftover = 0;
    leftover = abs(leftover) + NE[-1][0];
    min_level = NE[-1][1]+1;
    ans = max(leftover, min_level)
    out.write("Case #"+str(j+1)+": "+str(ans)+"\n")
out.close();

