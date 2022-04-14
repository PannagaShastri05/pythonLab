#Function overloading using a decorator called "multiple dispatch"

from multipledispatch import dispatch

class over:
	@dispatch(int, int)
	def product(first, second):
		result = first * second
		print(result)

	@dispatch(float, float)
	def product(first, second):
		result = first * second
		print(result)
	@dispatch(int, int, int)
	def product(first, second, third):
		result = first * second * third
		print(result)
	@dispatch(float, float, float)
	def product(first, second, third):
		result = first * second * third
		print(result)

ob1 = over()
print("-------------------------------------------------------------------------------------------")
print("                      ~  O  V  E  R  L  O  A  D  I  N  G ~                                 ")
print("-------------------------------------------------------------------------------------------")
while True:
	print("\n\n1.Two int parameters \n2.Two float parameters \n3.Three int parameters \n4.Three float parameters \n0.Exit\n")
	ch = int(input("Enter your choice: "))
	if ch==1:
		ob1.product(10, 10)
	elif ch==2:
		ob1.product(2.5, 2.5)
	elif ch==3:
		ob1.product(10, 10, 10)
	elif ch==4:
		ob1.product(2.5, 2.5, 2.5)
	elif ch==0:
		exit()
	else:
		print(" :( ----W R O N G  C H O I C E------ ): ")
