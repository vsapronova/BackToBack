
def buildings_with_view(buildings):
    max_height = -1
    queue = []
    for i in range(len(buildings)):
        if max_height < buildings[i]:
            queue.append(i)
            max_height = buildings[i]

    return queue



print(buildings_with_view([ 4, 6, 2, 3, 8]))