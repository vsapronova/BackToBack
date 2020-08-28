def nearest_distance(sentence):
    if len(sentence) < 2:
        return None
    last_seen_repeated = {}
    closest_dist = []
    for i in range(len(sentence)):
        word = sentence[i]
        if word in last_seen_repeated:
            closest_dist.append(i - last_seen_repeated[word])
        last_seen_repeated[word] = i
    return -1 if len(closest_dist) == 0 else min(closest_dist)


print(nearest_distance([
  "This",
  "is",
  "a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated",
    "a",
    "a"
]))