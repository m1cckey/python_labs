def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    return (min(nums), max(nums))


def unique_sorted(nums):
    return sorted(set(nums))


def flatten(mat):
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            return "TypeError"
        result.extend(item)
    return result


print("min_max:")
print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5, -2, -9]), sep="\n")
print(min_max([]), min_max([1.5, 2, 2.0, -3.1]), sep="\n")
print("unique_sorted:")
print(unique_sorted([3, 1, 2, 1, 3]), unique_sorted([]), sep="\n")
print(unique_sorted([-1, -1, 0, 2, 2]), unique_sorted([1.0, 1, 2.5, 2.5, 0]), sep="\n")
print("flatten:")
print(
    flatten([[1, 2], [3, 4]]),
    flatten(([1, 2], (3, 4, 5))),
    flatten([[1], [], [2, 3]]),
    sep="\n",
)
print(flatten([[1, 2], "ab"]))
