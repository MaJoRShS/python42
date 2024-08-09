#!/usr/bin/env python3

"""
Aqui é para você pegar o arquivo e abri-lo
legenda de parâmetros

Modos de Abertura
'r': Leitura (read). O arquivo deve existir. O arquivo é aberto apenas para leitura.
'w': Escrita (write). Cria um novo arquivo ou sobrescreve um arquivo existente.
'a': Adição (append). Abre o arquivo para escrita, mas adiciona o conteúdo ao final do arquivo sem sobrescrever o existente.
'b': Modo binário. Adiciona ao modo de abertura ('rb', 'wb', 'ab') para leitura ou escrita de arquivos binários.
'x': Criação exclusiva (exclusive creation). Cria um novo arquivo e lança uma exceção se o arquivo já existir.

"""

# Aqui eu to o arquivo como tem o r é read
# file = open('lorem.txt', 'r')
# print(f'file: {file.read()}')
# file.close()


# Aqui to lendo linha a linha e transformando a palavra Lorem para CHUCUPA
with open('lorem.txt', 'r') as file:
    while True:
        linhas = len(file.readlines())
        print(letra)
        if not linhas:
            break  # Sai do loop quando não há mais linhas
        # Processar a linha (por exemplo, imprimir)
        # print(linha, end='|ENDLINE|\n')

file.close()


# Aqui eu to escrevendo w é write dentro de um arquivo, mais o b.o é que ele sobrescreve o conteúdo que está la.
# with open('lorem.txt', 'w') as file:
#     file.write('lupaLinda. \n')
# file.close()