#Selection Sort
def sort(number):
    
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if number[j] < number[minpos]:
                minpos = j

        temp = number[i]
        number[i] = number[minpos]
        number[minpos] = temp

        print(number)

number = [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
sort(number)

print(number)