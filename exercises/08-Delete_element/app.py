#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    filtered = filter(lambda person: person != person_name,  people)
    return list(filtered)


# Funciona! Pero no pasa el test xq el test espera un if y un loop
people = ['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
