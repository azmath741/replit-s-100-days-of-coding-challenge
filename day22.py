import random as r
print("NUMBER GUESSING GAME!")
guess=r.randint(0,1000000)
count=0
while True:
 number=int(input("pick a number from 0 to 1000000:"))
 if number== guess:
   print("Your guess is correct,YOU WON!")
   count=count+1
   print(f"no .of guesses={count}")
   break
 elif number<guess:
  print("Your guess is too low")
  count=count+1

 elif number>=guess:
   print("Your guess is too high")
   count=count+1
 if number <0:
  print("invalid guess")
  exit()
 else:
  continue
