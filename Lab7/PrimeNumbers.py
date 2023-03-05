import numpy as numpy
def is_prime(n):
    if n < 2:
        return False
    for X in range(2, int(np.sqrt(n))+1):
        if n % X == 0:
            return False
    return True
numbers = numpy.array([2])
X = 3
while numbers.size < 15:
    if is_prime(X):
        numbers = numpy.append(numbers, X)
    X += 1
print(numbers)
