password=input("Enter the password:").strip()
has_number=False
for ch in password:
   if ch.isdigit():
       has_number=True
if len(password)>=8 and has_number :
    print("✅ Strong Password")
else:
     print("❌ Weak Password")