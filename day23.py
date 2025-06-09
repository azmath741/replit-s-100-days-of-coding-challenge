def login():
  while True:
    name=input("enter your name:")
    password=input("enter your password:")
    if name=="admin" and password=="admin":
      print("Welcome admin")
      break
    else:
      print("Invalid credentials")
      continue
print("REPLIT LOGIN SYSTEM")
login()