from unicodedata import name

res = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(res)