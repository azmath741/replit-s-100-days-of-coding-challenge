exit="no"
while exit == "no":
  animal_name=input("Enter the animal name: ").lower()
  if animal_name=="cow":
    print("The animal is moo.")
  elif animal_name =="tiger":
    print("the animal is roar.")
  elif animal_name =="cat":
    print("the animal is meow.")
  elif animal_name =="dog":
    print("the animal is bark.")
  else:
    print("The animal is not found.")
  exit=input("Do you want to exit? ").lower()
