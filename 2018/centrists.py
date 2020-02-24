t = int(input())
orders = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
for m in range(1,t+1):
    l = int(input())
    names = input().split(' ')
    boolAnswers= [False, False, False]
    for order in orders:
        sortedDict = {key: i for i, key in enumerate(order)}
        y = [[sortedDict[j] for j in name] for name in names]
        sortedNames = [x for _,x in sorted(zip(y, names))]
        if (sortedNames.index(names[0]) == 1):
            boolAnswers[0] = True
        if (sortedNames.index(names[1]) == 1):
            boolAnswers[1] = True
        if (sortedNames.index(names[2]) == 1):
            boolAnswers[2] = True
        if (boolAnswers[0] and boolAnswers[1] and boolAnswers[2]):
            break
    answers = []
    for ans in boolAnswers:
        if (ans):
            answers.append('YES')
        else:
            answers.append('NO')
    print('Case #{}: {} {} {}'.format(m, answers[0], answers[1], answers[2]))