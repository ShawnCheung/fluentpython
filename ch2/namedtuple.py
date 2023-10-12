from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 34.54, (34.32, 434.54))
print(tokyo)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 32, LatLong(23,32))
delhi = City._make(delhi_data)

delhi._asdict()