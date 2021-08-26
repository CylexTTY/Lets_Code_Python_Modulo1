def decToBin(decNumber: int, binaryStr='') -> str:
    if decNumber == 0:
        return binaryStr

    # Necessariamente aqui tem que ser o resto do numero por 2 + string binaria
    # anterior, nao podendo ser: binaryStr += str(decNumber % 2)
    binaryStr = str(decNumber % 2) + binaryStr
    return decToBin(decNumber // 2, binaryStr)

print(decToBin(233)) # 11101001
