import random

from insertion_srot import insertion_sort

bucket_num = 10


def bucket_sort(data):
    buckets = [[] for i in range(bucket_num)]
    for value in data:
        buckets[int(value * 10)].append(value)

    for bucket in buckets:
        insertion_sort(bucket)

    k = 0
    for bucket in buckets:
        for value in bucket:
            data[k] = value
            k += 1


if __name__ == '__main__':
    data = [random.uniform(0, 1) for i in range(20)]
    print(data)
    bucket_sort(data)
    print(data)
