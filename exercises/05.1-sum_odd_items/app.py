def sum_odds(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total += number
    return total

arreglo = [4, 5, 734, 43, 45, 100, 4, 56, 23, 67, 23, 58, 45]
print(sum_odds(arreglo))
