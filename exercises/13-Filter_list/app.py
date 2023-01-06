def filter_function(items):
    return items > 10


all_numbers = [23, 12, 35, 5, 3, 2, 3, 54, 3, 21, 534, 23, 42, 1]

# Implementación 1
greater_than = list(filter(filter_function, all_numbers))
print(greater_than)

# Implementación 1
greater_than = list(filter(lambda x : x > 10, all_numbers))
print(greater_than)
