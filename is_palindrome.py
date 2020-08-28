import math


def isPalindrome(x):

    if x < 0:
        return False
    if x == 0:
        return 0

    count_digits = math.log(x, 10)
    total = int(math.floor(count_digits) + 1)
    mask = int(math.pow(10, total - 1))

    for i in range(total // 2):
        first = x // mask
        last = x % 10

        if first != last:
            return False

        x %= mask
        x //= 10
        mask = mask / 100
    return True