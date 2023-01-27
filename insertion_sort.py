def insertion_sort(list):  
    for i in range(1, len(list)):  
        current = list[i]  

        j = i - 1  
        while j >= 0 and current < list[j]:  
            list[j+1] = list[j]  
            j -= 1  
        list[j+1] = current  

    return list


def main():
    list = [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
    insertion_sort(list)
    print(list)

main()