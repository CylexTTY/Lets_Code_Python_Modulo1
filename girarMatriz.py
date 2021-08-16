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
    match times:
        case _ if times % 4 == 0:
            return matriz
        case _ if ((times == 3 or times % 4 == 3) and times % 2 != 0):
            times = 3
        case _ if times % 2 == 0:
            times = 2
        case _:
            times = 1

    matriz_scope: list = [[] for _ in range(len(matriz[1]))]
    for j in range(len(matriz)-1, -1, -1):
        last = matriz.pop(j)
        for k, item in enumerate(last):
            matriz_scope[k].append(item)
    return girarMatriz(matriz_scope, times-1)


matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_rotacionada = girarMatriz(matriz_exemplo, 3)
# Mostrando:
for linha in matriz_rotacionada:
    print(linha)
