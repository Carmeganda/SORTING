#Bubble Sort
def sort(number):
    for i in range(len(number)-1,0,-1):
        for j in range(i):
            if number[j]>number[j+1]:
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp


number= [8, 78, 23, 62, 39, 36, 7, 50, 53, 15]
sort(number)

print(number)