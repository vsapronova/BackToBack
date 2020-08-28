def longest_pal(s):
    non_pairs = []
    count = 0
    for char in s:
        if char not in non_pairs:
            non_pairs.append(char)
        else:
            non_pairs.remove(char)
            count += 1
    if len(non_pairs) != 0:
        count = count*2 + 1
    else:
        return count*2
    return count



print(longest_pal("ccc"))
