import random


def quick_sort(data, start, end):
    if start >= end:
        return
    i = start
    j = end
    pivot = data[i]
    while i < j:
        while data[j] > pivot and j > i:
            j -= 1
        while data[i] <= pivot and i < j:
            i += 1
        if j > i:
            data[j], data[i] = data[i], data[j]
    data[start], data[i] = data[i], data[start]

    quick_sort(data, start, i - 1)
    quick_sort(data, i + 1, end)
    pass


if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    quick_sort(data, 0, len(data) - 1)
    print(data)
