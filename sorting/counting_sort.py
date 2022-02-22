import random

count_size = 10


def counting_sort(data):
    size = len(data)
    count = [0] * 10

    for i in range(0, size):
        count[data[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    output = [0] * size

    for value in data:
        output[count[value] - 1] = value
        count[value] -= 1

    for i in range(size):
        data[i] = output[i]


if __name__ == '__main__':
    data = [random.randrange(count_size) for i in range(20)]
    print(data)
    counting_sort(data)
    print(data)
