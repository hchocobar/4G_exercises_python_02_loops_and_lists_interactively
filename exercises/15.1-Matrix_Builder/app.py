# Implementación 1: comprehension standard
def matrix_builder_1(n):
    row = [1 for i in range(0, n)]  # Crea una lista con 'n' 1s
    matrix = [row for i in range(0, n)]  # Crea una lista con 'n' columnas
    return matrix


# Implementación 2: comprehension advanced 1
def matrix_builder_2(n):
    matrix = [[1 for i in range(0, n)] 
              for i in range(0, n)]
    return matrix


# Implementación 3: comprehension advanced 2
def matrix_builder_3(n):
    return [[1 for i in range(n)] for i in range(n)]  # Omito el 1er parametro de range()


# Invoco las funciones e imprimo
print(matrix_builder_1(5))
print(matrix_builder_2(4))
print(matrix_builder_3(3))
