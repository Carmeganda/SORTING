def partition(list, low, high):
    i = low
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] =  list[j], list[i]
            i += 1

    list[i], list[high] = list[high] ,list[i]

    return i


def quick_sort(list, low, high):
    if low < high:
        partition_index = partition(list, low, high)
        quick_sort(list, low, partition_index - 1)
        quick_sort(list, partition_index + 1, high)


def main():
    list = [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
    print(list)

    list = [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
    quick_sort(list, 0, len(list) - 1)
    print(list)

main()