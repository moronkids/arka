string = ""
bar = 1
z = 1
i = 1
x = int(input("Masukkan angka :"))

# Looping Baris
while bar <= x:
	kol = bar
	# Looping Kolom
	batas = kol - 1
	while kol > 0:
		if kol > 1:
			string = string + "   "
		else:
			string = string + " * "
		kol = kol - 1

	if bar == 1:
		string = string + " * " * ((x-z)*2)
	elif bar == x:
		string = string
	else :
		string = string + "   " * ((x-z)*2-1) + " * "


	z = z + 1
	string = string + "\n"
	bar = bar + 1
	i = i + 1
print (string)
