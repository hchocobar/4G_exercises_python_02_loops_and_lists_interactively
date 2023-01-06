names = ['Liam', 'Emma', 'Noah', 'Olivia', 'William', 'Ava', 'James', 'Isabella', 'Logan', 'Sophia',
         'Benjamin', 'Mia', 'Mason', 'Charlotte', 'Elijah', 'Amelia', 'Oliver', 'Evelyn', 'Jacob', 'Abigail',
         'Lucas', 'Harper', 'Michael', 'Emily', 'Alexander', 'Elizabeth', 'Ethan', 'Avery', 'Daniel', 'Sofia',
         'Matthew', 'Ella', 'Aiden', 'Madison', 'Henry', 'Scarlett', 'Joseph', 'Victoria', 'Jackson', 'Aria',
         'Samuel', 'Grace', 'Sebastian', 'Chloe', 'David', 'Camila', 'Carter', 'Penelope', 'Wyatt', 'Riley']

# El método .find() devuelve el índice de la subcadena encontrada. En caso de no encontrarla devuelve -1
filtered_names = list(filter(lambda x: x.find('am') != -1, names))
print(filtered_names)  # Salida: ['Liam', 'William', 'James', 'Benjamin', 'Samuel', 'Camila']

filtered_names = list(filter(lambda x: x.lower().find('am') != -1, names))
print(filtered_names)  # Salida: ['Liam', 'William', 'James', 'Benjamin', 'Amelia', 'Samuel', 'Camila']
