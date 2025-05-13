
print("Secure Login")
username = input("What is your username?")
password = input("What is your password?")

if username == "john" and password == "john000":
  print("Welcome, john! You are looking nice today!")
elif username == "harry" and password == "harry000":
  print("Hi harry! Love your hair today!")
elif username == "spider" and password == "spider000":
  print("Yo! spider! What up?!")
else:
  print("You do not have access. Go away!")