func = lambda n: (lambda f: f(n, f))(lambda n, f: n*f(n-1, f) if n else 1)

print(func(7))

"""Simple factorial function. I made this to explain the concept of recursion in oneliners."""
