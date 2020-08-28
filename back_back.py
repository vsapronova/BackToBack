

def count_digits(x):
    y = 10
    number = 1
    count = 0
    while number != 0:
        number = x // y
        y *= 10
        count += 1
    return count




