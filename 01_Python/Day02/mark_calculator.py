student_name=input("Enter student Name:")
english_mark=float(input("Enter your English Mark:"))
maths_mark=float(input("Enter your Maths Mark:"))
science_mark=float(input("Enter your Science Mark:"))

total=english_mark+maths_mark+science_mark
average=total/3

print("\n=======RESULTS========")
print("Student Name:",student_name)
print("English Mark:",english_mark)
print("Maths Mark:",maths_mark)
print("Science Mark:",science_mark)
print("Total Marks:",total)
print("Average Marks:",average)
