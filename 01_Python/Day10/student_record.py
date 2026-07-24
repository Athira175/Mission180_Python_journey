name=input("Enter studentname:")
course=input("Enter course:")

with open("student.txt","a") as file:
    file.write(f"\nName:{name}")
    file.write(f"\nCourse:{course}")
    file.write("\n---------------")
    print("file successfully created")
