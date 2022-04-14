while True:
	print("\n")
	print("                    ~ S E L E C T  F R O M  B E L O W ~                      ")
	print("\n")
	print("-------------------------------------")
	print("1.To check ValueError")
	print("2.To check FileNotFoundError")
	print("3.To check TypeError")
	print("4.To check IOError")
	print("5.To check NameError")
	print("0.To Exit The Program")
	print("-------------------------------------")
	print("\n")
	ch=int(input("Enter Your Choice : "))
	if ch==1:
		try:
			print("\n")
			print("> > > E x c e p t i o n < < <")
			print("\n")
			f=open("f1.txt","z")
			print("Inside The Try Block")
		except ValueError:
			print("You Are Facing A ValueError")
	elif ch==2:
		try:
			print("\n")
			print("> > > E x c e p t i o n < < <")
			print("\n")
			f=open("f.txt","r")
			print("Inside The Try Block")
		except FileNotFoundError:
			print("You Are Facing A FileNotFoundError")
	elif ch==3:
		try:
			print("\n")
			print("> > > E x c e p t i o n < < <")
			print("\n")
			f=open("f1.txt","r","w")
			print("Inside The Try Block")
		except TypeError:
			print("You Are Facing A TypeError")
	elif ch==4:
		try:
			print("\n")
			print("> > > E x c e p t i o n < < <")
			print("\n")
			f=open("f1","w+")
			f.write("sample")
			f.close()
			f1=open("f2","r")
			print("Inside The Try Block")
		except IOError:
			print("You Are Facing A IOError")
	elif ch==5:
		try:
			print("\n")
			print("> > > E x c e p t i o n < < <")
			print("\n")
			f=opens("f1.txt","r")
			print("Inside The Try Block")
		except NameError:
			print("You Are Facing A NameError")
	elif ch==0:
		exit()
	else:
		print("Wrong Choice")
