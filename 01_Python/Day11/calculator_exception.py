try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    print("Addition:",num1+num2)
    print("Division:",num1/num2)
    print("Multiplication:",num1*num2)
    print("Substraction:",num1-num2)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Invalid number.")
else:
    print("valid for all operations")
finally:
    print("Thank you for using calculator.")