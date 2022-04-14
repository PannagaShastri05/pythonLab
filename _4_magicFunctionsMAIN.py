from magic_code import*

ob1=operator()
ob2=operator()

ob1.accept()
ob2.accept()

while True:
	print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Floordivision \n5.Exit \n")
	ch=int(input("Enter your choice: "))
	if ch==1:
		ob1+ob2
	elif ch==2:
		ob1-ob2
	elif ch==3:
		ob1*ob2
	elif ch==4:
		ob1//ob2
	elif ch==5:
		exit()
	else:
		print("Invalid choice!--Chose between 1 and 5")

