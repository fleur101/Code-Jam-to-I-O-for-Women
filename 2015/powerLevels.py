# A multifactorial -- that is, a number N followed by some nonzero number E of exclamation points -- is defined as the product of all positive numbers (N - K*E) for which K is a nonnegative integer. Normal factorials meet the definition of multifactorials, for example:
# 5! = 5 * (5-1) * (5-2) * (5-3) * (5-4) = 120
# Here are the other multifactorials of 5:
# 5!! equals 5 * (5-2) * (5-4) = 15
# 5!!! equals 5 * (5-3) = 10
# 5!!!! equals 5 * (5-4) = 5
# 5 followed by five or more !s = 5
# 5 with no exclamation points is not considered a multifactorial.
# The villainous Anima and her underling Minera love three things: multifactorials, yelling "IT'S OVER 9000" followed by some number of exclamation points, and going around the universe looking for people to fight.
# When Anima and Minera encounter a potential opponent, Anima asks Minera to use her scanner device to determine the opponent's power level, which is always a positive integer that does not begin with any leading zeroes. Today, the display on Minera's scanner is blurry, and she can only tell Anima the number of digits D in the opponent's power level, and not what any of those digits are.
# Anima wants to yell IT'S OVER followed by a multifactorial of 9000 to accurately describe the opponent's power level. She will never yell something that might not be true, and she will never use more exclamation points than she needs to. For example, if D = 31682, Anima can't yell IT'S OVER 9000!, because she knows that 9000! also has 31682 digits and the opponent's power level might be a 31682-digit number that is less than or equal to 9000!. However, since 9000!! has fewer than 31682 digits, she can be confident that the opponent's power level is greater than 9000!!, so IT'S OVER 9000!! is guaranteed to be true. Although the opponent's power level is also definitely greater than 9000!!!, 9000!!!!, and so on, she won't use more exclamation points than she needs to. So, in this example, she will yell IT'S OVER 9000!!
# If there is no multifactorial of 9000 that is definitely less than the opponent's power level, Anima will remain dramatically silent. We represent dramatic silence as an ellipsis: ...
# What should Anima say?
import math
t = int(input()) 
for i in range(1, t + 1):
    d = int(input())
    if (d < 5):
        print("Case #{}: ...".format(i))
        continue
    nums = []
    res = 0
    for x in range (1, 9001):
        digits = 0
        for y in range(9000, 1, -x):
            digits += math.log10(y);
        num = math.floor(digits) + 1
        if (d>num):
            res = x
            break
    print("Case #{}: IT'S OVER 9000{}".format(i, '!'*res))