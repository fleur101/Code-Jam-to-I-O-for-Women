#  The owner of a prestigious ballroom has painted a beautiful circular clock on the dance floor, and a group of D dancers numbered 1 through D are about to literally "dance around the clock". They are standing in a circle, with dancer 1 at the 12:00 position of the circle and the other dancers going clockwise around the circle in increasing numerical order. The number of dancers is even.
# The dance will go on for N turns. On the i-th turn (counting starting from 1), the following will happen:
#     If i is odd, then the dancer currently at the 12:00 position will swap positions with the next dancer in clockwise order. Then, going past those two, the next pair of dancers in clockwise order will swap positions, and so on, all the way around the ring clockwise, until all dancers have participated in exactly one swap.
#     If i is even, then the dancer currently at the 12:00 position will swap positions with the next dancer in counterclockwise order. Then, going past those two, the next pair of dancers in counterclockwise order will swap positions, and so on, all the way around the ring counterclockwise, until all dancers have participated in a swap.
# For example, this diagram shows the initial state and two turns of a dance with eight people.
# Which two dancers will be next to dancer number K when the dance is over? 
t = int(input()) 
for i in range(1, t + 1):
    d, k, n = [int(s) for s in input().split(" ")] 
    n = n%d
    if (k%2 == 0):
        pos_k = (k-n)%d
        if (pos_k == 0):
            pos_k = d
        l = (pos_k-n-1)%d
        if (l == 0):
            l = d
        r = (pos_k-n+1)%d
        if (r == 0):
            r = d
    else:
        pos_k = (k+n)%d
        if (pos_k == 0):
            pos_k = d
        l = (pos_k+n-1)%d
        if (l == 0):
            l = d
        r = (pos_k+n+1)%d
        if (r == 0):
            r = d
    print("Case #{}: {} {}".format(i, r, l))