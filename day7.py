genre=input("which genre do you like most? action or comedy :").lower()
print()
if genre == "action":
    print("you should watch the movie 'Die Hard'")   
    if genre != "action":
        print("you are not  a super fan of action    movies")
    else:
      print("you are a super fan of action movies")
elif genre == "comedy":
    print("you should watch the movie 'Free Guy'")
    if genre != "comedy":
        print("you are not  a super fan of comedy movies")
    else:
      print("you are a super fan of comedy movies")
else:
  print("invalid genre")