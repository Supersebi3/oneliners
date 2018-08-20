func = lambda n: (lambda f: f(n, f))(lambda n, f: 1 if n < 3 else f(n - 1, f) + f(n - 2, f))

print(func(7))

"""Fibonacci number generator by Bamboo"""
