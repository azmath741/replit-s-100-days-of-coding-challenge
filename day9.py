yearOfBirth=int(input("enter your year of birth:"))
if yearOfBirth>=1925 and yearOfBirth<=1946:
    print("you are a traditionalist")
elif yearOfBirth>=1947 and yearOfBirth<=1964:
    print("you are a baby boomer")
elif yearOfBirth>=1965 and yearOfBirth<=1981:
    print("you are a generation x")
elif yearOfBirth>=1982 and yearOfBirth<=1995:
    print("you are a millenial")
elif yearOfBirth>=1996 and yearOfBirth<=2015:
    print("you are a generation z")
else:
  print("you are a generation alpha")