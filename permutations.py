import copy

def perm(array):
    perms = []
    generate_perm([], array, perms)
    return perms


def generate_perm(choices, array, perms):
    if len(choices) == len(array):
        perms.append(copy.deepcopy(choices))
        return

    for i in range(len(array)):
        choice = array[i]
        if choice in choices:
            continue
        choices.append(choice)
        generate_perm(choices, array, perms)
        choices.pop()


print(perm([1, 2, 3]))