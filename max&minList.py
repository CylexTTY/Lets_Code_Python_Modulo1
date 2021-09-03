def maxList(lista, count=0):
    num_list = [maxList(el)
                if isinstance(el, list) else el
                for el in lista]
    maior = [n for n in num_list if False not in [n >= num for num in num_list]]
    if count == 0:
        return maior[0]
    elif count == 1:
        return maior[0], len(maior)


def minList(lista, count=0):
    num_list = [minList(el)
                if isinstance(el, list) else el
                for el in lista]
    menor = [n for n in num_list if False not in [n <= num for num in num_list]]
    if count == 0:
        return menor[0]
    elif count == 1:
        return menor[0], len(menor)
