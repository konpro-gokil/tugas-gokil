pertama = {"keju", "tepung", "garam", "gula"}
print(pertama)
kedua = {"garam", "gula", "coklat", "kecap"}
print(kedua)
kedua.add("keju")
print(kedua)
c = pertama & kedua
print(c)
d = pertama.difference(kedua)
print(d)
e = pertama.discard("garam")
print(e)
f = kedua.difference(pertama)
print(f)
g = pertama.symmetric_difference(kedua)
print(g)
for data in pertama:
	print(data)
for data in kedua:
	print(data)