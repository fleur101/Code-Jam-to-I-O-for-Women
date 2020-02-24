#  You are a casting director for an upcoming musical. The musical has N roles, and for each role, you want to cast two performers: one primary performer and one understudy. A primary performer or understudy trains for only one particular role, and the job of the understudy is to play the role if the primary performer becomes unavailable. At least one of the two performers for each role must be available for the show to succeed.
# You have selected 2N performers to be in the musical. They are all quite talented, and any of them can be cast as a primary performer or understudy for any of the roles. However, you are worried that some of them may be tempted to run away to join the cast of Hamiltonian!, the smash hit musical about quantum mechanics, before your show opens. Luckily, you are an excellent judge of character. You know that the i-th performer has a probability Pi of becoming unavailable. (These probabilities are all independent of each other, and a given performer has their probability regardless of their assigned role or whether they are a primary performer or understudy.)
# You wish to assign one primary performer and one understudy for each role in a way that maximizes the probability that the show will succeed. That is, you want to minimize the probability that there will be at least one role for which the primary performer and understudy both become unavailable.
# If you make optimal casting choices, what is the probability that your show will succeed? 
t = int(input())
for i in range(1,t+1):
    n = int(input())
    probs = [float(x) for x in input().split()]
    probs.sort()
    revProbs = probs[::-1]
    res = 1
    for x in range(n):
        avProb = 1 - probs[x]*revProbs[x]
        res*=avProb
    print('Case #{}: {}'.format(i, res))