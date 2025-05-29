print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

startingNO=int(input("Enter the starting number:"))
endingNO=int(input("Enter the ending number:"))
inc=int(input("Enter the increment:"))
for i in range(startingNO,endingNO,inc):
    print(i)