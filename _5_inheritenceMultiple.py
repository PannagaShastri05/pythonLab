class student:
	def __init__(self):
		self.usn = input("Enter usn :")
		self.name = input("Enter name :")
		self.age = int(input("Enter age:"))

	def display(self):
		print("USN :",self.usn)
		print("Name :",self.name)
		print("Age :",self.age)

class ugstudent(student):
	def __init__(self):
		student.__init__(self)
		self.sem = input("Enter semester :")
		self.fees = int(input("Enter fees :"))
		self.stipend = int(input("Enter stipend :"))
		ugstudent.display(self)

	def display(self):
		student.display(self)
		print("Semester :",self.sem)
		print("Fees :",self.fees)
		print("Stipend :",self.stipend)

class pgstudent(student):
	def __init__(self):
		student.__init__(self)
		self.sem = input("Enter semester :")
		self.fees = int(input("Enter fees :"))
		self.stipend = int(input("Enter stipend :"))
		pgstudent.display(self)

	def display(self):
		student.display(self)
		print("Semester :",self.sem)
		print("Fees :",self.fees)
		print("Stipend :",self.stipend)

while True:
	print("\n\n1.UG_student \n2.PG_student \n3.exit \n")
	ch=int(input("Enter your choice :"))
	if ch == 1:
		ug=ugstudent()
	elif ch == 2:
		pg=pgstudent()
	elif ch == 3:
		exit()
	else:
		print("Wrong choice!")


