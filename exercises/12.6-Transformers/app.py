incoming_ajax_data = [{"name": 'Mario', "last_name": 'Montes'},
                      {"name": 'Joe', "last_name": 'Biden'},
                      {"name": 'Bill', "last_name": 'Clon'},
                      {"name": 'Hilary', "last_name": 'Mccafee'},
                      {"name": 'Bobby', "last_name": 'Mc birth'}]

# Your code go here:
full_name = list(map(lambda person: person['name'] + ' ' + person['last_name'], incoming_ajax_data))
print(full_name)  # Salida: ['Mario Montes', 'Joe Biden', 'Bill Clon', 'Hilary Mccafee', 'Bobby Mc birth']
