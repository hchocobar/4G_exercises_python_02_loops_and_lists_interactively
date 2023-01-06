def prepender(name):
    return "My name is: " + name


names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan']
new_list = map(prepender, names)
print(list(new_list))
#Your code go here: