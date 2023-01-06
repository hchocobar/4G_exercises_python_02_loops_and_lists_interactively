all_colors = [{"label": 'Red', "sexy": True},
              {"label": 'Pink', "sexy": False},
              {"label": 'Orange', "sexy": True},
              {"label": 'Brown', "sexy": False},
              {"label": 'Pink', "sexy": True},
              {"label": 'Violet', "sexy": True},
              {"label": 'Purple', "sexy": False}]

# Implementación 1: 
# Primero el filter(), luego el map() 
filtered = list(filter(lambda x: x['sexy'], all_colors))
mapped = list(map(lambda x: '<li>' + x['label'] + '</li>', filtered))
print(mapped)  # Salida: ['<li>Red</li>', '<li>Orange</li>', '<li>Pink</li>', '<li>Violet</li>']

# Implementación 2: 
# Los dos pasos en la misma función
html = list(map(lambda x: '<li>' + x['label'] + '</li>', filter(lambda x: x['sexy'], all_colors)))
print(html)  # Salida: ['<li>Red</li>', '<li>Orange</li>', '<li>Pink</li>', '<li>Violet</li>']
