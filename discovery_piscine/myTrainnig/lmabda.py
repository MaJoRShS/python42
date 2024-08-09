notas = {'Ana': 9, 'Beto': 7, 'Carlos': 8}

""" 
Aqui o Sorted tem syntax ao contrario, 
você passa item iteravél e depois o que vai ser feito
e qual é a chave que vai ser utilizada para ser ordenada.
"""
notas_ordenadas = sorted(
    notas.items(),
    key=lambda tupla: tupla[1]
)

print(f'notas_ordenadas: {notas_ordenadas}')

"""
Aqui tem que colocar a notas.items() porque eu tenho uma 
tupla e ai para devolver ela como lista precisa disso, e aqui
precisa ser uma filtragem mesmo.
"""
notas_add = filter(lambda tupla: tupla[1] > 7 ,notas.items())

print(f'list(notas_add): {list(notas_add)}')

"""
Aqui é uma lambda inline que na teoria só roda uma unica vez para um unico registro.
"""
a = 6
se = lambda x: x if x > 7 else "Error"
print(se(a))