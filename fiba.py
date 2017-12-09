fiba = [0,1]
num = input ("masukkan jumlah deret fibonacci= ")
num = int (num)

if num < 3:
	print("minimal 3 deret")
else:
	for i in range (num-2) :
		fiba.append(fiba[-2]+fiba[-1])
		print(fiba)