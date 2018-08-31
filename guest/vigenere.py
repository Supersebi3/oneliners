func = lambda word, key, decode=False: (lambda word, key, m, n: ''.join([*map(chr, map(lambda x, y: (((x - 18) % 26 + (1 if not decode else -1) * ((y - 18) % 26) - 1) % 26) + 97, map(ord, word), map(ord, (key * (m // n)) + key[:m % n])))]))(word.lower(), key.lower(), len(word), len(key))

print(func("vigenere", "abc"))

"""Vigenere cipher by Bamboo."""
