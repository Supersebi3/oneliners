func = lambda n, k: (lambda f: f(n, k, f))(lambda n, k, f: 0 if k > n else 1 if k == 0 or n == 1 else f(n - 1, k - 1, f) + f(n - 1, k, f))

print(func(5, 2))

"""The mathematical choose thingy by Bamboo"""
