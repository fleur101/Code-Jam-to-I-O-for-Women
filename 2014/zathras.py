#  It is year 2025 on planet Zathras -- a world populated exclusively by semi-sentient robots called Zathrinians. There are two kinds of Zathrinians: acrobots and bouncoids. Once a year, the Great Mind makes its Great Decision for that year, and chooses how the Zathrinians will reproduce and be decommissioned. When it's making the Great Decision, it takes into account two Eternal Parameters: α and β. These parameters, being Eternal, do not change from year to year.
# Reproduction: If there are A acrobots and B bouncoids when the Great Mind makes the Great Decision, the Great Mind will create K = min(A, B) reproductive pairs by pairing together an acrobot and a bouncoid. Any remaining robots will be unpaired. The next day, 2% of those K couples (rounded down) will produce one baby Zathrinian each.
# Out of all the baby Zathrinians produced, α% (rounded down) are acrobots, and β% (rounded down) are bouncoids. The remaining baby Zathrinians are split evenly between acrobots and bouncoids; if there's an odd number, the extra baby becomes a bouncoid. 
def calc(a,b,alpha,beta, y):
    if (y == 0):
        return num_a, num_b
    dec_a = a//100
    dec_b = b//100
    num_couples = min(a, b)
    num_babies = num_couples // 50
    num_a = num_babies // alpha
    num_b = num_babies // beta
    rem = num_babies - num_a - num_b
    num_a += rem // 2
    num_b += rem // 2
    if (rem % 2 != 0):
        num_b += 1
    return calc(num_a, num_b, alpha, beta, y-1)
    
t = int(input()) 
for m in range(1, t + 1):
    a, b, alpha, beta, y = [int(x) for x in input().split()]
    num_a, num_b = calc(a, b, alpha, beta, y)
    print("Case #{}: {} {}".format(m, num_a, num_b))