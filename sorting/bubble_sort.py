import random


def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


if __name__ == '__main__':
    data = [random.randrange(100) for i in range(20)]
    print(data)
    bubble_sort(data)
    print(data)
