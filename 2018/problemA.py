f = open('A-large-practice.in', 'r')
#f = open('input.txt', 'r')
T = int(f.readline())
out = open("output.txt", "w");

for j in range (T):
    N = int(f.readline()); 
    distances = [int(x) for x in f.readline().split(" ")];
    distances.sort(reverse=True);
    ideal = [];
    for i in range(N):
        if i%2 == 0:
            ideal.insert(0, distances[i]);
        if i%2 == 1:
            ideal.append(distances[i]);
    original = list(range(int((N+N%2)/2))) + list(reversed(range(int(N/2))));
    error = sum([(ideal[i]-original[i])**2 for i in range(N)])
    out.write("Case #"+str(j+1)+": "+str(error)+"\n")
out.close();

