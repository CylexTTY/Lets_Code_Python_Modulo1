class Fibonacci(object):

    def findIdx(self, n):
        if n == 1:
            return 0
        if n <= 3:
            return 1
        return self.findIdx(n - 1) + self.findIdx(n - 2)

    def sequence(self, n_numbers):
        return [self.findIdx(i) for i in range(n_numbers+1)][1:]

fib = Fibonacci()
print(fib.findIdx(10))
print(fib.sequence(10))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, ...
# 1  2  3  4  5  6  7  8   9   10  11  12  13   14   15   16   17   18    ...
