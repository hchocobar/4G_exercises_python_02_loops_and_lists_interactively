def my_function(numbers):
    new_list = []
    for number in numbers:
        #The magic go here:
        if number == 1:
            new_list.append(number)
        else:
            new_list.append('Yahoo')
    return new_list


my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]
print(my_function(my_list))


