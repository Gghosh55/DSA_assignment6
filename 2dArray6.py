from collections import Counter


def find_original_array(change):
    count_map = Counter(change)
    original = []

    for num in change:
        if count_map[num] > 0 and count_map[num // 2] > 0:
            original.append(num // 2)
            count_map[num] -= 1
            count_map[num // 2] -= 1
        else:
            return []

    return original
change = [1, 3, 4, 2, 6, 8]

print(find_original_array(change))
