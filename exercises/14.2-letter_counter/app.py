# Implementación 1: standard
def check_frequency_1(x):
    frequency = {}
    for c in set(x):
       frequency[c] = x.count(c)
    return frequency


# Implementación 2: comprehension
def check_frequency_2(x):
    return {c: x.count(c) for c in set(x)}



paragraph = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
print(check_frequency_1(paragraph.lower()))
print(check_frequency_2(paragraph.lower()))
