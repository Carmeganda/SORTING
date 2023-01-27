def merge_sort(list):

    if len(list) <= 1:
        return list

    midpoint = int(len(list) / 2)

    left, right = merge_sort(list[:midpoint]), merge_sort(list[midpoint:])

    return merge(left, right)


def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer += 1

        else:

            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


def main():
    list = [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
    print(list)

    result = merge_sort(list)
    print(result)

if __name__ == "__main__":
    main()