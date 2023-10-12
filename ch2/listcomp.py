symbols = "?*&$#(%)"
codes = [ord(ch) for ch in symbols if ord(ch) > 40]
print(codes)

out = list(filter(lambda x: x>40, map(ord, symbols)))
print(out)
print(list(map(ord, symbols)))