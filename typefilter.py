func = lambda module, *types: list(filter((lambda a: isinstance(a, types)), [getattr(module, name) for name in dir(module)]))

print(func(__import__('math'), float))

"""Find all attributes of `module` (can really be any type that has a dir()) that match the given type(s)."""
