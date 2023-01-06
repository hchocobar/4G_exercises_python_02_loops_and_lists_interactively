def merge_list(list1, list2):
    #Your code go here:
    return list1 + list2


chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']

# Funciona! Porque la función retorna la suma (concatenación) de dos listas.
# No pasa el test, xq el test espera un for
print(merge_list(chunk_one, chunk_two))
