# Our computers are so excited about the upcoming Google I/O that they've started storing their ones as capital letter Is and their zeroes as capital letter Os! For example, the character A, which is 65 in ASCII, would normally be stored as the byte 01000001, but our computers are storing it as OIOOOOOI.
# Given a string of 8-character "bytes" consisting of Is and Os, can you translate it using ASCII? Every "byte" is guaranteed to translate to a printable character (a decimal value between 32 and 126, inclusive). Note that one of these characters (the one with decimal value 32) is a space. No translated message will begin or end with a space, but there may be internal space characters. 
t = int(input()) 
for i in range(1, t + 1):
    b = int(input())
    chs = input()
    bin = chs.replace('I', '1')
    bin = bin.replace('O', '0')
    bin_list = [bin[i:i+8] for i in range(0, len(bin), 8)]
    res = ''
    for bin in bin_list:
        if (len(bin) == 8):
            ascii = int(bin, 2)
            res += chr(ascii)
    print("Case #{}: {}".format(i, res))