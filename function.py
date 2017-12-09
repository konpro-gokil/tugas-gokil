# function luas lingkaran
def luas_lingkaran(r):
	luas = phi*(r**2)
	return luas

#function keliling lingkaran
def keliling_lingkaran(r):
	keliling = 2*phi*r
	return keliling

# fungsi untuk pilihan	
def option():
	print("pilih salah satu dari tiga functionlitas berikut:")
	print("1. mencari luas lingkaran")
	print("2. mencari keliling lingkaran")
	print("3. keluar dari program")
	pilihan = int(input("masukan pilihan anda:"))
	return pilihan
	
# main program
phi = 3.14
pilihan = True
while(pilihan<3):
	pilihan = option()
	if(pilihan==1):
		r = int(input("masukan jari:"))
		l = luas_lingkaran(r)
		print("luas lingkaran: %.2f"%(l))
	elif(pilihan==2):
		r = int(input("masukan jari:"))
		k = keliling_lingkaran(r)
		print("keliling lingkaran: %.2f"%(k))