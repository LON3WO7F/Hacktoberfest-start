def bubble_sort(list):

    for number in range(len(list)-1,0,-1):
        for num in range(number):
            if list[num]>list[num+1]:
                temp = list[num]
                list[num] = list[num+1]
                list[num+1] = temp


list = [10,8,13,90,14,23,40,76,89,50]
bubble_sort(list)
print(list)
