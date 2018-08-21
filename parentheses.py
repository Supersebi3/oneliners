func = lambda s: not (lambda f: f(s, f, 0, 0))(lambda s, f, sum, i: True if sum < 0 else sum+0 if i == len(s) else f(s, f, (1 if s[i] == '(' else -1) + sum, i+1))

print(func('()()'))
print(func('(()())'))
print(func('()(())'))
print(func(')(()'))
print(func('((())'))

"""My really bad recursive parentheses validator."""
