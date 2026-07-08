name=input("Enter your name:")
mark=float(input("Enter your mark:"))



print("Name of the student :",name)
print("Mark:",mark)
if mark>=90:
    Grade ="A"
elif mark>=80:
    Grade ="B"
elif mark>=70:
     Grade ="C"
elif mark>=60:
     Grade ="D"
else:
     Grade ="F"
if mark>=40:
    status="PASSED"
else:
    status = "FAILED"
print("Grade:",Grade)
print("Status:",status)
