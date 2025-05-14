genre=input("which genre do you like most? action or horror/comedy :").lower()
print()
if genre == "action":
    print("you should watch the movie'Bahubali'") 
    hero= input("who is a main role in the bahubali movie  ? prabhas or ranveer singh :").lower()
    if  hero == "prabhas":
      print("you are  a super fan of action movies")

    else:
      print("you are not a super fan of action movies")
elif genre == "horror/comedy":
    print("you should watch the movie 'stree 2'")
    hero= input("who is the man that shown in the climex of the movie  ? varun dhawan or ram charan :").lower()
    if hero == "varun dhawan":
        print("you are  a super fan of horror/comedy movies")
    else:
      print("you are not a super fan of horror/comedy movies")
else:
  print("invalid genre")
