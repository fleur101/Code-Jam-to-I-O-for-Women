#  On a distant moon of Jupiter, some developer conference events are about to happen! They are called IO (uppercase I, uppercase O), Io (uppercase I, lowercase o), iO (lowercase I, uppercase O), and io (lowercase I, lowercase O).
# The best way to advertise an event is by using special computers that print the event's name one character at a time, with the output appearing on a digital display. Each such computer only knows the name of one event, and is programmed to print its event's name zero or more times. For example, a computer programmed to print IO twice prints an I, followed by an O, followed by an I, followed by an O, for a final string of IOIO.
# You know that the conference organizers are using these computers, but you do not know how many computers are advertising each event. For each event, there may be any number of computers (including zero) programmed to print the event's name. Moreover, the computers are not necessarily all programmed to print the same number of times. For example, it is possible that there are three computers programmed to print Io once each, and one computer programmed to print Io twice.
# The computers have all finished printing, but unfortunately, they all printed to the same display! Because the computers printed concurrently, event names in the final output string may be interleaved. You are considering the possible ways in which that string could have been produced.
# For example, the string IiOioIoO could have been produced by two computers, as follows:
#     A: programmed to print Io twice
#     B: programmed to print iO twice
#     index:  1 2 3 4 5 6 7 8
#     A:      I . . . o I o .
#     B:      . i O i . . . O
#     string: I i O i o I o O
# In this interpretation, the Io event was advertised twice, the iO event was advertised twice, and the other two events were not advertised at all.
# But the string could have also been produced by three computers:
#     A: programmed to print IO twice
#     B: programmed to print io once
#     C: programmed to print io once
#     index:  1 2 3 4 5 6 7 8
#     A:      I . O . . I . O
#     B:      . i . . o . . .
#     C:      . . . i . . o .
#     string: I i O i o I o O
# In this interpretation, the IO event was advertised twice, the io event was advertised twice, and the other two events were not advertised at all. Notice that this interpretation required two computers printing io; there could not have been just one computer printing io twice, because it would have had to print i twice in a row, which is not allowed.
# Given a final output string, what is the maximum possible number of times that the event IO could have been advertised?
# It is guaranteed that the string has at least one valid interpretation. For example, oI and IOI are not valid inputs. 
t = int(input()) 
for m in range(1, t + 1):
    s = input()
    ises = list()
    num = 0
    for i in range(len(s)):
        if (s[i] == 'I' or s[i] == 'i'):
            ises.append(s[i])
        elif (s[i] == 'O'):
            if ('I' in ises):
                ises.remove('I')
                num+=1
                continue
            else:
                ises.remove('i')
        elif (s[i] == 'o'):
            if ('i' in ises):
                ises.remove('i')
            else:
                ises.remove('I')
    print("Case #{}: {}".format(m, num))