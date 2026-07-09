students=[]
while True:
    print("==========STUDENT MANAGEMENT=========")
    print("1.ADD STUDENT")
    print("2.VIEW STUDENT")
    print("3.REMOVE STUDENT")
    print("4.EXIT")

    print("SELECT THE CHOICE 1-4")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        name=input("Enter the student name:")
        students.append(name)
        students.sort()
    elif choice ==2:
        for display in students:
            count=1
            print(count,".",display)
            count=count+1
    elif choice ==3:
        remove_name=input("Enter the student name to remove: ")
        if remove_name in students:
            students.remove(remove_name)
            print("Student removed successfully.")
        else :
            print("Student not found.")
    elif choice ==4:
        print("THANK YOU!")
        break
    else:
        print("Invalid choice! Please enter 1 to 4.")

