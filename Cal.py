def sum(x, y):
	return x+y
def sub(x, y):
	return x-y
def mul(x, y):
	x*y 
def div(x,y):
	x/y 
print ("Choice def.")
print ("1.sum")
print ("2.sub")
print ("3.mul")
print ("4.div")

choice = input("Enter choice(1/2/3/4):")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == '1':
   print(a,"+",b,"=", sum(a,b))

elif choice == '2':
   print(a,"-",b,"=", sub(a,b))

elif choice == '3':
   print(a,"*",b,"=", mul(a,b))

elif choice == '4':
   print(a,"/",b,"=", div(a,b))
else:
   print("Invalid input")