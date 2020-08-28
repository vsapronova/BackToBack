
# Given a set of strings words and a string pattern return a list of all of the strings in words
#  that matches the pattern of the pattern string.


def findAndReplacePattern(words, pattern):
    '''
    :type words: list of str
    :type pattern: str
    :rtype: list of str
    '''
    matches = []
    for word in words:
        if word_match(word, pattern):
            matches.append(word)
    return matches


def word_match(word, pattern):
    if len(word) != len(pattern):
        return False
    else:
        word_to_pattern = [0] * 256
        pattern_to_word = [0] * 256
        ascii_char = [ord(c) for c in word]
        ascii_pattern = [ord(c) for c in pattern]
        for i in range(len(ascii_char)):
            if word_to_pattern[ascii_char[i]] == 0:
                word_to_pattern[ascii_char[i]] = ascii_pattern[i]
            if pattern_to_word[ascii_pattern[i]] == 0:
                pattern_to_word[ascii_pattern[i]] = ascii_char[i]
            if word_to_pattern[ascii_char[i]] != ascii_pattern[i] or pattern_to_word[ascii_pattern[i]] != ascii_char[i]:
                return False

    return True


print(findAndReplacePattern(["abc","cde","zzz"],"aaa"))