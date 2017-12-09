tuple_a = (1,2,3,4,5)
print("alamat: ",id(tuple_a),",before: ", tuple_a)
tuple_a += (6,)
print("alamat: %i"%(id(tuple_a)),",after: %s" %(tuple_a,))


print("data index ke %i isinya : %i" %(tuple_a.index(2),tuple_a[1]))