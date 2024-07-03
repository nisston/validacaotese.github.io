# -*- coding: utf-8 -*-
"""02_Pratica_1_Lista

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMGIYJtX_y8n8r1VgkyT_-O_Z-ko2Km3

# Trabalhando com Listas no Python

Aqui vamos apresentar todos os tópicos discutidos em sala de aula pelo professor, com uma ou duas células com exemplos práticos da aplicação do comando ou recurso. A seguir a lista de tópicos trabalhados:

* Introdução às lista em Python (criação de uma lista)
* Acesso a elementos de uma lista
* Operações básicas com listas (adição, remoção, alteração)
* Métodos de listas em Python (append(), extend(), insert(), remove(), etc.)
* Iteração sobre elementos de uma lista (loops for e while)
* Indexação e fatiamento de listas
* Listas aninhadas (listas dentro de listas)
* Compreensão de lista (list comprehension)
* Ordenação de listas
* Filtragem com filter()

Para maiores informações segue um pequeno tutorial: [Tutorial List no Python](https://docs.python.org/3/tutorial/datastructures.html)

# Introdução às Lista em Python (criação de uma lista)
"""

# Criando uma lista vazia
lista_vazia = []

# Criando uma lista com elementos
numeros = [1, 2, 3, 4, 5]
nomes = ["João", "Maria", "Pedro"]

"""# Acesso a elementos da lista"""

numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Acessando o primeiro elemento da lista (índice 0)
print(numeros[-1])  # Acessando o último elemento da lista

"""# Operações básica com listas:"""

numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros.append(6)  # Adicionando um elemento ao final da lista
print(numeros)

numeros.remove(3)  # Removendo um elemento da lista
print(numeros)

numeros.reverse()  # Invertendo a ordem dos elementos na lista
print(numeros)

"""# Iteração sobre elementos de uma lista"""

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

"""# Métodos de lista:"""

numeros = [1, 2, 3, 4, 5]
print(len(numeros))  # Retorna o tamanho da lista
print(numeros.index(3))  # Retorna o índice do primeiro elemento com o valor 3
print(numeros.count(2))  # Retorna o número de ocorrências do valor 2 na lista

numeros = [9, 20, 13, 4, 45]
print(numeros)
numeros.pop(2)
print(numeros)

numeros = [9, 20, 13, 4, 45]
print(numeros)
numeros.clear()
print(numeros)

numeros = [9, 20, 13, 4, 45]
numeros.sort()
numeros

numeros = [9, 20, 13, 4, 45]
numeros.append(50)
numeros

# Lista original
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]

numeros1.extend(numeros2)

# Imprimindo lista1 após a extensão
print(numeros1)

numeros = [9, 20, 13, 4, 45]
numeros.insert(1,25)
numeros

numeros = [9, 20, 13, 4, 45]
numeros.remove(13)
numeros

"""# Indexação e fatiamento de listas:"""

numeros = [1, 2, 3, 4, 5]
print(numeros[1])  # Acessando o segundo elemento da lista (índice 1)
print(numeros[2:4])  # Fatiando a lista para obter elementos do índice 2 ao 3
print(numeros[2:])  # Fatiando a lista para obter elementos do índice 2 até o final
print(numeros[:4])  # Fatiando a lista para obter elementos do índice 0 até o 3
print(numeros[:])  # Fatiando a lista para obter todos os elementos

"""# Listas aninhadas (listas dentro de listas):"""

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_aninhada[1][2])  # Acessando o elemento na segunda lista e terceiro elemento
print(lista_aninhada[0][1])  # Acessando o elemento na primeira lista e segundo elemento
print(lista_aninhada[2][0])  # Acessando o elemento na terceira lista e primeiro elemento
print(lista_aninhada[1][0])  # Acessando o elemento na segunda lista e primeiro elemento

"""# Compreensão de listas (list comprehension):"""

numeros = [1, 2, 3, 4, 5]
print(numeros)
quadrados = [x**2 for x in numeros]  # Lista com os quadrados dos números
print(quadrados)

"""# Ordenação de listas:"""

numeros = [3, 1, 4, 2, 5]
print(numeros)
numeros.sort()  # Ordenando a lista
print(numeros)

numeros = [3, 1, 4, 2, 5]
print(numeros)
numeros.sort(reverse=True)  # Ordenando a lista
print(numeros)

"""# Filtragem de listas com expressões lambda e filter():

## Trabalhando com filter
"""

def eh_negativo(x):
    return x < 0

numeros = [-3, -2, -1, 0, 1, 2, 3]
numeros_neg = list(filter(eh_negativo, numeros))
print(numeros_neg)

def eh_string_longa(s):
    return len(s) > 5

strings = ["apple", "banana", "grape", "orange", "kiwi", "watermelon"]
strings_longa = list(filter(eh_string_longa, strings))
print(strings_longa)  # Saída: ['banana', 'orange', 'watermelon']

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Saída: [2, 4, 6, 8, 10]

"""## Trabalhando com filer e lambda"""

numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # Filtrando os números pares
print(pares)

numeros = [15, 20, 25, 30, 35, 40, 45, 50]
divisivel_por_3_e_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numeros))
print(divisivel_por_3_e_5)

values = [10, None, 20, None, 30, None, 40]
non_null_values = list(filter(lambda x: x is not None, values))
print(non_null_values)

numbers = [-3, -2, -1, 0, 1, 2, 3]
negative_numbers = list(filter(lambda x: x < 0, numbers))
print(negative_numbers)

strings = ["apple", "banana", "grape", "orange", "kiwi", "watermelon"]
long_strings = list(filter(lambda x: len(x) > 5, strings))
print(long_strings)  # Saída: ['banana', 'orange', 'watermelon']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Saída: [2, 4, 6, 8, 10]