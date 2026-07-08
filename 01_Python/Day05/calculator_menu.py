def add(n1,n2):
    print(f"sum of {n1}+{n2}:{n1+n2}")
def substract(n1,n2):
    print(f"substraction of {n1}-{n2}:{n1-n2}")
def multiply(n1,n2):
    print(f"multiplication of {n1}*{n2}:{n1*n2}")
def division(n1,n2):
    if n2==0:
        print("Error:invalid not divided by zero")
    else:
        print(f"division of {n1}/{n2}:{n1/n2}")

print("========Calculator============")
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
c=int(input("choose number :"))
if c == 1:
    add(num1,num2)
elif c == 2:
    substract(num1,num2)
elif c==3:
    multiply(num1,num2)
elif c==4:
    division(num1,num2)
else:
    print("Invalid choice! Please choose between 1 and 4.")
