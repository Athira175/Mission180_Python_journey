student={}
student["name"]=input("Enter your name:")
student["age"]=int(input("Ente your age:"))
student["course"]=input("Enter your course:")
student["city"]=input("Enter your city:")

print("\n----STUDENTS DETAILS--------")
for key,value in student.items():
    print(f"{key}:{value}")