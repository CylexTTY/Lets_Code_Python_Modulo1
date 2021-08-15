"""
Objetivo:
Girar matriza noventa graus, sentido horário.

matriz original:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz final:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
"""


def girarMatriz(matriz: list, times: int = 1) -> list:
    """
    Rotaciona a matriz noventa graus sentido horário 'n' vezes.
    :param matriz: matriz solicitada.
    :param times: quantidade de vezes que a matriz será rotacionada.
    :return: matriz rotacionada.
    """
    if times % 4 == 0:
        return matriz
    elif (times % 3 == 0 or times % 4 == 3) and times % 2 != 0:
        times = 3
    elif times % 2 == 0:
        times = 2
    else:
        times = 1

    for _ in range(times):
        matriz_scope: list = [[] for _ in range(len(matriz[1]))]
        for _ in range(len(matriz)):
            last = matriz.pop(-1)
            for i, item in enumerate(last):
                matriz_scope[i].append(item)
        matriz = matriz_scope
    return matriz


matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_rotacionada = girarMatriz(matriz_exemplo, 5)

# Mostrando:
for linha in matriz_rotacionada:
    print(linha)
