names = ['Esmeralda', 'Kiko', 'Ruth', 'Lebron', 'Pedro', 'Maria', 'Lou', 'Fernando', 'Cesco', 'Bart', 'Annie']

#Your code here:
names[1] = 'Steven'
names[-1] = 'Pepe'
names[0] = names[2] + names[4]

# Funciona! No pasa el test, xq el test espera que utilice range()
for name in names[::-1]:
    print(name)
