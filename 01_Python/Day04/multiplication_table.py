num=int(input("Enter the start number :"))
num2=int(input("Enter the end number:"))
for j in range(num,num2+1):
    print("=====MULTIPLICATION TABLE OF "f"{num}============")
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
    num=num+1
