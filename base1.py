#function untuk menyimpan data
def menyimpan_biodata(nama, asal, tanggal):
	file = open("base.txt","a+")
	result = file.write("nama saya adalah %s\n"%(nama))
	result = file.write("saya berasal dari %s\n"%(asal)
	result = file.write("saya lahir pada %s\n"%(tanggal))
	
#function tampilkan semua data
def tampilkan_semua_biodata(nama, asal, tanggal):
	file = open("database.txt","r")
	print("==menampilkan biodata==")
	print(file.read())
	
# fungsi untuk pilihan	
def option():
	print("pilih salah satu dari tiga functionlitas berikut:")
	print("1. menyimpan biodata")
	print("2. tampilkan semua biodata")
	print("3. keluar dari program")
	pilihan = int(input("masukan pilihan anda:"))
	return pilihan

#main program	
pilihan = True
while(pilihan<3):
	pilihan = option()
	if(pilihan==1):
		nama = str(input("masukan nama: "))
		asal = str(input("masukan asal: "))
		tanggal = str(input("masukan tanggal: "))
		menyimpan_biodata(nama, asal, tanggal)
		print("menyimpan_data:"(a))
	elif(pilihan==2):
		tampilkan_semua_biodata()