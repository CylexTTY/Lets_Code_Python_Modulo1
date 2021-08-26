def sumList(*args):
    return sum(sumList(*el) if isinstance(el, list) else el for el in args)


print(sumList([1, 2, 3], 1, [1, [2, [3], [4, 5]]])) # 22
