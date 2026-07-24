try:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enterr the second number:"))
    print("Result:",num1/num2)
    age=int(input("Enter the Age:"))
    print("Age:",age)
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")


    age=int(input("Enter the Age:"))
    print("Age:",age)
except ValueError:
    print("❌ Please enter numbers only.")
else:
    print("Valid")

finally:
    print("Program finished")
