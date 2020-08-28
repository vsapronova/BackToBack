

def add_binary(s1, s2):
    if len(s1)==0 and len(s2)==0:
        return None
    digit1 = 0
    for i in range(len(s1)-1, -1, -1):
        if s1[i]=='1':
            digit1 += 2**(len(s1)-1-i)
    digit2 = 0
    for j in range(len(s2)-1, -1, -1):
        if s2[j]=='1':
            digit2 += 2**(len(s2)-1-j)
    sum_digits = digit1 + digit2

    return "{0:b}".format(sum_digits)


print(add_binary('1010', '1'))