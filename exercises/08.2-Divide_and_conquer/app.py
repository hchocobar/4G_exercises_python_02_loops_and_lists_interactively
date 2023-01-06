def merge_two_list(numbers):
    odd = filter(lambda x : x % 2 == 1, numbers)
    even = filter(lambda x : x % 2 == 0, numbers)
    return [list(odd), list(even)]

# Funciona! Pero no pasa el test, xq el teste espera un 'for'
list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]
print(merge_two_list(list_of_numbers))  # Salida: [[85, 59, 37, 25, 5, 81, 41, 55], [4, 80, 64, 66, 20, 64, 22, 76, 76, 96, 2, 68]]
