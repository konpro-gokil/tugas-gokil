print("a")
a = ["wiliam", "kate", "anderson", "jame", "mady"]
print(a)

print("b")
a+=["jones",]
print(a)

print("c")
a = ["wiliam", "kate", "anderson", "jame", "mady","jones"]
a[2]= "grace"
print(a)

print("d")
a = ["wiliam", "kate", "grace", "jame", "mady","jones"]
member = "thompson" not in a
print(member)

print("e")
a = ["wiliam", "kate", "grace", "jame", "mady","jones"]
print("a: ",sorted(a))

print("f")
a = ["wiliam", "kate", "grace", "jame", "mady","jones"]
for x in a:
	print("a: ",x)
	
print("g")
a = ["wiliam", "kate", "grace", "jame", "mady","jones"]
a.clear()
print(a)