func = lambda s: (lambda ns, n: '\n'.join([(' '*i) + (' '*(n-1)).join([c for j, c in enumerate(ns) if j%n==i]) for i in range(n)]))(''.join(map((lambda a: f'{a:<{max(map(len, s.split()))}}'), s.split())), max(map(len, s.split())))

print(func("this is a test"))

"""Print out text in a pretty weird way. Ask Bamboo (who suggested this) why."""
