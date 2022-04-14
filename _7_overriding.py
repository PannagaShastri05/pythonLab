class Employee:
	def __init__(self, first, last, empid):
		self.first=first
		self.last=last
		self.empid=empid
		self.pay=int(input("Enter the salary : "))
		print("\n")
	def display(self):
		print("FirstName: ",self.first)
		print("LastName: ",self.last)
		print("Empid: ",self.empid)
		print("\n")
		print(">>>>>>>My Final Pay: ",self.pay)
		print("\n")
	def pay_raise(self):
		self.rise=1.5
		self.pay=int(self.pay)*self.rise
class Developer(Employee):
	def pay_raise(self):
		self.rise=2.5
		self.pay=int(self.pay)*self.rise
class Manager(Employee):
	def pay_raise(self):
		self.rise=3.5
		self.pay=int(self.pay)*self.rise

print("\n\n")
print("*************************************************")
print("              ~ O V E R R I D E ~            ")
print("*************************************************\n\n")
while True:
	print("\n1.Employee \n2.Developer \n3.Manager \n4.Exit \n")
	ch = int(input("Enter your choice :"))
	if ch==1:
		e1=Employee("akash","akash",101)
		print("                  - A K A S H -                   \n")
		print("---------------------------------------------------")
		print("Payment i got is : ",e1.pay)
		print("---------------------------------------------------")
		if e1.pay<15000:
			print("Employee payment should be more than 15k\n")
		else:
			e1.pay_raise()
			e1.display()
		print("\n")
	elif ch==2:
		d1=Developer("arjun","arjun",102)
		print("                - A R J U N -                   \n")
		print("---------------------------------------------------")
		print("Payment i got is : ",d1.pay)
		print("---------------------------------------------------")
		if d1.pay<25000:
			print("Developer payment should be more than 25k\n")
		else:
			d1.pay_raise()
			d1.display()
		print("\n")
	elif ch==3:
		m1=Manager("anjuman","anjuman",103)
		print("                - A N J U M A N -                   \n")
		print("---------------------------------------------------")
		print("Payment i got is : ",m1.pay)
		print("---------------------------------------------------")
		if m1.pay<50000:
			print("Manager payment should be more than 50k\n")
		else:
			m1.pay_raise()
			m1.display()
	elif ch==4:
		exit()
	else:
		print("wrong choice")
