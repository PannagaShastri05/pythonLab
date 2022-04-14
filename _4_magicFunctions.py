class operator:
	def __init__(self):
		self.l1=[]
	def accept(self):
		n=int(input("Enter number of elements : "))
		for i in range(0, n):
			ele=int(input("Enter the element : "))
			self.l1.append(ele)
		print("List : ",self.l1)
	def __add__(self, other):
		newlist=[]
		for i in range(0, len(self.l1)):
			newlist.append(self.l1[i]+other.l1[i])
		print("After the addition : ",newlist)
	def __sub__(self, other):
		newlist=[]
		for i in range(0, len(self.l1)):
			newlist.append(self.l1[i]-other.l1[i])
		print("After the subtraction : ",newlist)
	def __mul__(self, other):
		newlist=[]
		for i in range(0, len(self.l1)):
			newlist.append(self.l1[i]*other.l1[i])
		print("After the multiplication : ",newlist)
	def __floordiv__(self, other):
		newlist=[]
		for i in range(0, len(self.l1)):
			newlist.append(self.l1[i]//other.l1[i])
		print("After the floordivision : ",newlist)
