#PROGRAM EKSEKUSI WHILE
nama = ""

# konsep while (akan melakukan perulangan), hingga
# counter dari while terpenuhi, counter --> nama

# apabila nama tidak sama dengan python
while nama != "python":
	# apabila (nama!="python") = true
	# maka kode dibawah akan dijalankan
	nama = str(input("Masukan Nama : "))
	print("Nama Saya ",nama)
	if nama == "python":
		print("Goodbye ",nama)
		