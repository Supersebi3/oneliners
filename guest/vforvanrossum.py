func = lambda s: (lambda s: (lambda s, n: '\n'.join(f'{s[i] if i == n//2 else s[i] + " " * (n - (2 * i) - 2) + s[-i - 1]: ^{n + 2}}' for i in range((n // 2) + 1)))(s, len(s)))(s if len(s) % 2 else s + '?')

print(func("sebi"))

"""Collab between Bamboo and Dusty.P. Don't ask me what they did :shrug:"""
