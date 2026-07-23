employee={}
employee["Employee Name"]=input("Enter the employee name:")
employee["Employee ID"]=int(input("Enter the Employee ID:"))
employee["Department"]=input("Enter your department:")
employee["Salary"]=float(input("Enter your salary:"))

print("\n------EMPLOYEE DETAILS-----")
for key,value in employee.items():
    print(f"{key}:{value}")