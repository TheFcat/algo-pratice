import random


def merge_sort(data):
    if len(data) <= 1:
        return
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    merge_sort(data)
    print(data)
