#  Cody, the owner of the legendary Cody's Jams store, is planning a huge jam sale. To make things simple, he has decided to sell every item in his store at a 25% discount — that is, each item's sale price is exactly 75% of its regular price. Since all of his regular prices happened to be integers divisible by four, his sale prices are conveniently also all integers.
# To prepare for the sale, he placed an order to print new labels for all of his items at their sale prices. He also placed an order to print new labels for all of his items at their regular prices, to use once the sale is over.
# Cody just came back from picking up his order. Unfortunately, the printer gave him both orders in one combined stack, sorted by price. Both the sale price and the regular price label for each item are present somewhere in the stack. However, both types of labels look the same, and since he does not remember the price of every item, he is not sure which labels are the sale price labels. Can you figure that out?
# For instance, if the regular prices were 20, 80, and 100, the sale prices would be 15, 60, and 75, and the printer's stack would consist of the labels 15, 20, 60, 75, 80, and 100. 
t = int(input()) 
for j in range(1, t + 1):
    n = int(input())
    prices = [int(s) for s in input().split(" ")] 
    sales = []
    i = 0
    while(len(prices) > 0 and i<2*n):
        reg = prices[i]*4//3
        if (reg in prices):
            sales.append(prices[i])
            prices.remove(reg)
            prices.remove(prices[i])
        else:
            i+=1
    print("Case #{}: {}".format(j, " ".join(map(str, sales))))