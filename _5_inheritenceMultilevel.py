d={}
class student:
	def __init__(self):
		self.usn=input("Enter usn :")
		self.name=input("Enter name :")
		self.age=int(input("Enter age:"))
	def display(self):
		print("USN :",self.usn)
		print("Name :",self.name)
		print("Age :",self.age)

class derived1(student):
	def __init__(self):
		student.__init__(self)
		self.sem=input("Enter semester :")
		self.sub = []
		self.total=0
		for i in range(5):
			m=int(input("Enter the subject mark :"))
			self.sub.append(m)
			self.total += m
		self.per=(self.total/500)*100
		derived1.display(self)
	def display(self):
		student.display(self)
		print("Semester :",self.sem)
		for i in range(5):
			print("Subject mark is :",self.sub[i])
		print("Total marks :",self.total)
		print("Percentage :",self.per)


class derived2(derived1):
	def __init__(self):
		derived1.__init__(self)
		d.update({self.name :{
			"name":self.name,
			"usn":self.usn,
			"age":self.age,
			"semester":self.sem,
			"sub_marks":self.sub,
			"total_marks":self.total,
			"percentage":self.per
		}})
def printtmp():
	for key in d:
		print(key, d[key])

while True:
	print("\n\n1.Add_Records \n2.Display \n3.Exit \n")
	ch=int(input("Enter your choice :"))
	if ch==1:
		d2=derived2()
	elif ch==2:
		printtmp()
	elif ch==3:
		exit()
	else:
		print("Wrong choice!")
