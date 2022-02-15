import random


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key


if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    insertion_sort(data)
    print(data)
