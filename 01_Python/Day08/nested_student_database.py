student={
    1:{
        "name":"ATHIRA",
        "course":"MCA",
        "city":"Kottayam"
    },
    2:{
        "name":"AKHIL",
        "course":"BCA",
        "city" :"KOllam"   
    },
    3:{
        "name":"ANN",
        "course":"Nursing",
        "city":"irland"
    }

}
print("Student Details")
for roll_number,details in student.items():
    print("Roll Number:",roll_number)
    print("Name:",details["name"])
    print("Course:",details["course"])
    print("City:",details["city"])
    print("----------------------------")