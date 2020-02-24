# Eric Googlander is a fashion model who performs by walking around on a stage made of squares that form a grid with R rows and C columns. He begins at the leftmost bottom square, facing toward the top edge of the stage, and he will perform by making a series of moves. Googlander knows only the following two moves:
# 1. Take one step forward in the direction he is currently facing
# 2. Make a single 90 degree turn to the right, then take one step forward in the new direction he is facing following the turn
# (Note that Googlander does not know how to make a 90 degree left turn.)
# If a move would take Googlander off of the stage or onto a square he has already visited, that move is unfashionable. Whenever Googlander is in a position for which neither of the two possible moves is unfashionable, he is free to choose either move (independently of any other choices he has made in the past), but he must choose one of them. Whenever one of the possible moves he can make is unfashionable, he must make the other move. If at any point both of the possible moves are unfashionable, the show immediately ends without Googlander making another move. Note that Googlander cannot stop the show early -- he must keep moving until both possible moves become unfashionable.
# How many different paths is it possible for Googlander to walk? (Two paths are the same if and only if they visit the same squares in the same order.)
t = int(input()) 
for m in range(1, t + 1):
    r,c = [int(x) for x in input().split()]
    if (r==1 or c==1):
        print("Case #{}: {}".format(m, 1))
        continue
    stage = [[0 for j in range(c)] for i in range (r)]
    for j in range(c):
        stage[0][j] = 1
    for i in range(r):
        stage[i][0] = 1
    for i in range (1, r):
        for j in range(1, c):
            stage[i][j] = stage[i-1][j] + stage[i][j-1]
    print("Case #{}: {}".format(m, stage[r-1][c-1]))