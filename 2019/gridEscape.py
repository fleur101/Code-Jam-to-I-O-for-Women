#  You are designing a new "escape" adventure that uses a rectangular grid of rooms (unit cells) with R rows and C columns. Each room has four doors oriented in the four orthogonal directions of the grid: north, south, east, and west. The doors on the border of the grid lead outside, and all of the other doors lead to other rooms.
# The adventure will be played by exactly R × C players, with each player starting in a different one of the R × C rooms. Once everyone is in position and the game starts, all of the doors close, and there is a mechanical trick: one of the four doors in each room can be opened from inside the room, and the other three doors cannot be opened. This remains consistent throughout the adventure; in a given room, it is always the same door that can be opened. Notice that it is possible that a door that connects two rooms might be able to be opened from one side but not the other.
# Each player moves independently of all other players. Players can only go through doors that they opened themselves, and they must close doors behind them. Each player will keep going through doors until they go through a door that leads outside (and therefore they escape), or they have made R × C moves without escaping (at which point they are considered to have failed, and they do not escape).
# You want to choose which door in each room can be opened, such that exactly K of the players will be able to escape. Can you find a way to do this, or determine that it is IMPOSSIBLE? 
T = int(input())

def nnd(p, C):
	if (p % C == C-1):
		return "S"
	if (p % (2*C) < C):
		return 'E'
	return "W"

for i in range(1, T+1):
    R, C, K = [int(x) for x in input().split(' ')]
    if (K == R*C - 1):
        print('Case #{}: IMPOSSIBLE'.format(i))
        continue
    print('Case #{}: POSSIBLE'.format(i))
    res = ''
    even = "N" + "W"*(C-1)
    odd = "N" + "E"*(C-1)
    for i in range(R):
    	res += even if i%2==0 else odd
    if (K!=R*C):
    	res = res[:K]+ nnd(K, C) + res[K+1:]
    # print(res)
    for i in range(R):
    	print(res[i*C:i*C+C] if i%2==0 else res[i*C:i*C+C][::-1] )