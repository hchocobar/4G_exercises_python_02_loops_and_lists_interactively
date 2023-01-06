my_list = [3423, 5, 4, 47889, 654, 8, 867543, 23, 48, 56432, 55, 23, 25, 12]

#Your code here:
inicial = 7
stop = 14
increase = 1

for i in range(inicial, stop):
    if i == my_list[i]:
        i += increase
    print(my_list[i])
