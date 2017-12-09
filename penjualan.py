nama=input("masukan nama barang: ")
harga=int(input("masukan harga barang: "))
jumlah=int(input("masukan jumlah barang: "))
total=harga*jumlah
print("total harga",nama,"anda adalah Rp.",total)
pembayaran=int(input("masukan pembayaran: "))
hutang=total-pembayaran
if (pembayaran>total):
	print("jumlah kembalian anda adalah Rp.",pembayaran-total)
else:
	print("anda memiliki hutang",hutang)