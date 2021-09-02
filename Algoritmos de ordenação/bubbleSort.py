import random


def bubbleSort(lista):
    for _ in range(len(lista) - 1):
        for i in range(1, len(lista)):
            if lista[i - 1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print('Shuffle list:', lista)
print('Ordered list:', bubbleSort(lista))
