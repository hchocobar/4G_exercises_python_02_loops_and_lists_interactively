all_names = ["Romario", "Boby", "Roosevelt", "Emiliy",  "Michael",  "Greta",  "Patricia",  "Danzalee"]

#Your code go here:
resulting_names = list(filter(lambda x : x.startswith('R'), all_names))
print(resulting_names)  # Salida: ['Romario', 'Roosevelt']
