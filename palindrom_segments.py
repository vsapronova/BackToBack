


def palindrome(my_string):
    temp = [[]]
    result = []
    for char in my_string:
        if char in temp:
            new_segment = char + char
            result.append(new_segment)
            temp.remove(char)
        else:
            temp.append([char])
    for ch in temp:
        result.append(ch)
    return result


print(palindrome("aab"))