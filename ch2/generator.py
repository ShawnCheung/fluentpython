symbols = "#$%^&*()"
print(tuple(ord(ch) for ch in symbols))

import array

print(array.array('I', (ord(ch) for ch in symbols)))