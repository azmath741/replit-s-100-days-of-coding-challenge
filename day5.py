#hello there today i am going to build a ""Which character are you?" Generator"
#In this project i use sepcially if else statements
#this is going to be a fun little project that i am going to build
print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use yes and no.")
print()
spiderman=input("Do you like 'hanging around'?").lower()
korg=input("Do you have a 'gravelly' voice?").lower()
captain_marvel=input("Do you often feel 'Marvelous'?").lower()
thanos=input("do you like to erase ?").lower()
if spiderman=="yes":
  print("your spiderman")
else:
    print("you are not spiderman")
if korg=="yes":
  print("you are korg")
else:
    print("you are not korg")
if captain_marvel=="yes":
  print("you are captain marvel")
else:
    print("you are not captain marvel")
if thanos=="yes":
    print("you are thanos")
else:
    print("you are not thanos")
  
if spiderman=="yes" or korg =="yes" or captain_marvel=="yes" or thanos=="yes":
    print("you are a marvel character")
else:
    print("you are not a marvel character")