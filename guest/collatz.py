collatz = lambda n: (lambda n, l: (lambda f: f(n, f))(lambda n, f: (1 if n == 1 else f(n // 2, f) if not n % 2 else f(3 * n + 1, f)) and l.insert(0, n) or l))(n, [])


for i in [213, 421, 132459, 8923, 29, 2048, 321, 1097432, 129]:
    print(collatz(i), end='\n\n===================================================\n\n')

"""Collatz conjecture by Bamboo."""
