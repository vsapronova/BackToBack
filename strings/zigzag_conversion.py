def zigzag(s, rows):
    '''
    :type s: str
    :type rows: int
    :rtype: str
    '''
    if len(s) < 1 or rows < 1:
        return None
    str_list = [''] * rows
    down = True
    row = 0
    for char in s:
        str_list[row] += char
        if row == 0:
            down = True
        if row == rows - 1:
            down = False

        if rows > 1:
            if down:
                row += 1
            else:
                row -= 1

    result = ''
    for string in str_list:
        result += string

    return result


print(zigzag('YELLOW', 1))