print("1")
dict = {"mady":"8","roger":"5","paul":"5","lucy":"7"}
print(dict)

print("2")
dict = {"kekn":"8","andrea":"7","smith":"6"}
print(dict)

print("3")
dict = {"mady":"8","roger":"5","paul":"5","lucy":"7"}
new_dict = {"kekn":"8","andrea":"7","smith":"6"}
dict.update(new_dict)
print(dict)

print("4")
dictionary = {"roger":"5","paul":"5","smith":"6"}
new_dict = dict.fromkeys(dictionary,"8")
print(new_dict)

print("5")
dict = {"mady":"8","roger":"8","paul":"8","lucy":"7","kekn":"8","andrea":"7","smith":"8"}
for data in dict:
	print(data)