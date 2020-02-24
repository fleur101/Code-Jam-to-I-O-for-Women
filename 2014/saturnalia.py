# It is the eve of Saturnalia in the Roman Empire, and Caterina is preparing the stables for the next day's chariot race. Part of her job is to write instructions and notes, print them on her printer (she's ahead of her time), and put them on the stable walls. That's simple, but because Saturnalia is an important festival, she wants to make them beautiful. Caterina needs a computer program that reads a message and outputs it back, decorated with a box. The program needs to be able to handle many messages at once. Can you help her? 
t = int(input()) 
for m in range(1, t + 1):
    text = input()
    str1 = '+'+ '-'*(len(text) + 2) + '+'
    str2 = '| ' + text + ' |'
    ans = '\n' + str1 +'\n' + str2 + '\n' + str1
    print("Case #{}: {}".format(m, ans))