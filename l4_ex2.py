source = [-10, 50, 8, 12, 62, 1.1, 0.75, 120, 2500, 25.0]
print([item for i, item in enumerate(source[1:], 0) if item>source[i]])