import math

def num(n):
    return 1

def logarithm(n):
    return math.log10(n)

def lineal(n):
    return n

def n_logarithm(n):
    return n * math.log10(n)

def square(n):
    return n**2

def exponential(n):
    return 2**n


if __name__ == "__main__":
    n = [10, 100, 1000, 1000000]
    for value in n:
        print(num(value))
        print(logarithm(value))
        print(lineal(value))
        print(n_logarithm(value))
        print(square(value))
        print(exponential(value))
        print('\n')

