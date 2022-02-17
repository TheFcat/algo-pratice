import random


def selection_sort(data):
    for i in range(len(data) - 1):
        key = i
        for j in range(i, len(data)):
            if data[key] > data[j]:
                key = j
        data[i], data[key] = data[key], data[i]


if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    selection_sort(data)
    print(data)
