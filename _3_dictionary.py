dict = {}
class Employee:
	basic = 0.0
	def putinfo(self):
		name = input("Enter your name: ")
		addr = input("Enter your address: ")
		pan = input("Enter your pan number: ")
		basic = float(input("Enter your basic salary: "))
		da = 0.2*basic
		hra = 0.12*basic
		tds = 0.05*basic
		other = 0.05*basic
		gross = da+hra+basic
		deductions = tds+other
		netpay = gross-deductions
		dict.update({
			"name": name,
			"address": addr,
			"pan number": pan,
			"basic salary": basic,
			"da": da,
			"hra": hra,
			"tds": tds,
			"other tax": other,
			"gross salary": gross,
			"deduction": deductions,
			"netpay": netpay,
			})

	def search(self,key):
		if key in dict.keys():
			print(dict.get(key))
		else:
			print("The ke element not found!!!")

	def getinfo(self):
		print("EMPLOYEE DETAILS: ")
		print("NAME: ",dict.get("name"))
		print("ADDRESS: ",dict.get("address"))
		print("PAN NUMBER: ",dict.get("pan number"))
		print("BASIC SALARY: ",dict.get("basic salary"))
		print("DA: ",dict.get("da"))
		print("HRA: ",dict.get("hra"))
		print("TDS: ",dict.get("tds"))
		print("OTHER TAX: ",dict.get("other tax"))
		print("GROSS SALARY: ",dict.get("gross salary"))
		print("DEDUCTIONS: ",dict.get("deduction"))
		print("NETPAY: ",dict.get("netpay"))

emp = Employee()
while True:
	print("\n\n 1.ENTER DETAILS AND UPDATE \n 2.SEARCH \n 3.DISPLAY \n 4.EXIT \n")
	ch = input("Enter your choice: ")
	if ch=='1':
		emp.putinfo()
		print("record inserted!!")
	elif ch=='2':
		s = input("enter the key value to be searched: ")
		emp.search(s)
	elif ch=='3':
		emp.getinfo()
	elif ch=='4':
		exit()
	else:
		print("the choice is invalid")





