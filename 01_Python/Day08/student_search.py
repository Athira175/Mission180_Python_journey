students={
    1:{"name":"Athira","course":"MCA","city":"Kottayam"},
    2:{"name":"Akhil","course":"BCA","city":"Kollam"},
    3:{"name":"Ann elsa","course":"Nursing","city":"Irland"}

}
while True:
    print("=============== STUDENT DATABASE ==============")
    print("1.VIEW ALL STUDENTS")
    print("2.SEARCH STUDENT")
    print("3.EXIT")

    print("SELECT THE CHOICE 1-3")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        for roll_number,details in students.items():
            print("Roll Number:",roll_number)
            print("Name:",details["name"])
            print("Course:",details["course"])
            print("City:",details["city"])
            print("-------------------------------")
    elif choice ==2:
        roll=int(input("Ente the roll number:"))
        if roll in students:
            print("Student found")
            print("name:",students[roll]["name"])
            print("Course:",students[roll]["course"])
            print("City:",students[roll]["city"])
        else:
            print("❌ Student Not Found")

    elif choice ==3:
        print("THANK YOU!")
        break
    else:
        print("Invalid choice! Please enter 1 to 3.")


