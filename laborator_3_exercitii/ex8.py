data="2023-04-24 09:03:32.744178"
extrage_anul = lambda s: s[0:4]
extrage_luna = lambda s: s[5:7]
extrage_ziua = lambda s: s[8:10]
extrage_ora = lambda s: s[11:20]
print(extrage_anul(data))
print(extrage_luna(data))
print(extrage_ziua(data))
print(extrage_ora(data))