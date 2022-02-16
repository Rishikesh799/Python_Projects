#Create Calculator of two number by using python.

print("WELCOME TO CALCULATOR")
#for addtion of two no:
def suma(x,y):
    a=x+y
    return a
#for subtraction of two number:
def subt(x,y):
    a=x-y
    return a
#for multiplication of two numbers:
def mul(x,y):
    a=x*y
    return a
#for dividation of two numbers:
def div(x,y):
    a=x/y
    return a
def po(x,y):
    a=x**y
    return a

print("Select the proper option for every computation.")
print("1 for summation")
print("2 for subtraction")
print("3 for multiplication")
print("4 for dividetion")
print("5 for power")

user=float(input("Enter computation no you need:"))

if user==1.0:
    x=float(input("Enter your first digit:"))
    y=float(input("Enter your Second digit:"))
    print(suma(x,y))
    
elif user==2.0:
    x=float(input("Enter your first digit:"))
    y=float(input("Enter your Second digit:"))
    print(subt(x,y))
    
elif user==3.0:
    x=float(input("Enter your first digit:"))
    y=float(input("Enter your Second digit:"))
    print(mul(x,y))
    
elif user==4.0:
    x=float(input("Enter your first digit:"))
    y=float(input("Enter your Second digit:"))
    print(div(x,y))
    
elif user==5.0:
    x=float(input("Enter your first digit:"))
    y=float(input("Which power required enter those digit:"))
    print(po(x,y))
