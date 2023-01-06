def fahrenheit_values(x):
    # Fromula: (0°C × 9/5) + 32 = 32°F
    return (x * 9 / 5) + 32


celsius_values = [-2, 34, 56, -10]

# Implementación 1
result = list(map(fahrenheit_values, celsius_values))
print(result)

# Implementación 2
result = list(map(lambda x : (x * 9 / 5) + 32, celsius_values))
print(result)
