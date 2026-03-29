dict = {i:i*i for i in range(10)}
print(dict)
sir ="sdljkfjqekfjherthuerqhbwgmfvmgjehqrgheg"
dict2 ={i:sir.count(i) for i in sir}
print(dict2)
dict3 = { i : [x for x in range(1, i+1) if i%x == 0] for i in range(1, 11) }
print(dict3)