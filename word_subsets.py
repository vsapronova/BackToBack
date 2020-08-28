import copy

def word_subsets(words, subsets):
    result = []
    b_count = [0]*26
    for word in subsets:
        temp_count = count(word)
        for i in range(0, 26):
            if temp_count[i] > b_count[i]:
                b_count[i] = temp_count[i]
    for word in words:
        word_count = count(word)
        universal = True
        for i in range(0, 26):
            if b_count[i] > word_count[i]:
                universal = False
        if universal:
            result.append(word)

    return result


def count(word):
    if len(word) < 1:
        return None
    output = [0]*26
    for char in word:
        ind = ord(char) - ord('a')
        output[ind] += 1
    return output


print(word_subsets(["padding", "css", "randomcs"], ["cs", "c"]))