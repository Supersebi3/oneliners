func = lambda s, toggle=False: (lambda lsta: '\n'.join([f" {ln}" if i%2 == toggle else ln for i, ln in enumerate(lsta)]))((lambda lst: ['   '.join([w[i] for w in lst]) for i in range(max(map(len, lst)))])((lambda ls: [f"{i:<{max(map(len, ls))}}" for i in ls])(s.split())))

print(func("this is another example"))

"""Another weird text printer. Ask Bamboo how he gets all those ideas."""
