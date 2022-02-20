import random


def heapify(data, data_length, i):
    l = i * 2 + 1
    r = i * 2 + 2
    largest = i
    if l < data_length and data[largest] < data[l]:
        largest = l
    if r < data_length and data[largest] < data[r]:
        largest = r

    if largest != i:
        data[largest], data[i] = data[i], data[largest]
        heapify(data, data_length, largest)


def heap_sort(data):
    data_length = len(data)
    # build max_heap
    for i in range(data_length // 2 - 1, -1, -1):
        heapify(data, data_length, i)

    for i in range(data_length - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)


if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    heap_sort(data)
    print(data)
