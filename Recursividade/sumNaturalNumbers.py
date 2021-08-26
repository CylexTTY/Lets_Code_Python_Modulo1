def sumNum(num):
    """
    Calcula num + (num - 1) + ...
    """
    return num + sumNum(num-1) if num > 1 else num


print(sumNum(10))
