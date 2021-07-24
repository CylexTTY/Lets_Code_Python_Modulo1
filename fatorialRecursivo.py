def fatorial(n):
    if n == 0:
        return 1
    n *= fatorial(n-1)
    return n

print(fatorial(0))