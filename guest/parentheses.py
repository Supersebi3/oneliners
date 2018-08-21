func = lambda s: s.count('(') == s.count(')') and (lambda g: all(s.count(')') <= s.count('(') for s in g))(s[:i] for i, _ in enumerate(s))

print(func('()()'))
print(func('(()())'))
print(func('()(()'))
print(func('()(())'))
print(func('((()))'))
print(func('())('))
print(func('((()))()())))()'))
print(func('((())())()()((()))'))

"""Bamboo's way better parentheses validator."""
