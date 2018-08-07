func = lambda s, r=False: ' '.join([first+rest for first, rest in zip(((lambda lst: lst.insert(0, lst.pop()) or lst)([i[0] for i in s.title().split()]) if not r else __import__('random').sample([i[0] for i in s.title().split()], len([i[0] for i in s.title().split()]))), [i[1:] for i in s.title().split()])])

print(func("Guido van Rossum", r=True))

"""Swap first letters of words, either by going around in a cycle, or randomly."""
