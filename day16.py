#  lyrics:
# Baby, I like your style

# Grips on your waist
# Front way, back way
# You know that I don't play
# Streets not safe
# But I never run away
# Even when I'm away
# Oti, oti, there's never much love when we go OT
# I pray to make it back in one piece
# I pray, I pray
counter=1
while True:
    print("Fill in the blank lyrics!")
    print("(Type in the blank lyrics and see if you are as cool as me.)")
    l1=input("Baby, I ____ your style?").lower()
    l2=input("Grips on ____ waist?").lower()
    l3=input("Front way, ____ way?").lower()
    l4=input("You know that I don't ____?").lower()
    l5=input("Streets ___ safe?").lower()
    l6=input("But I never ___ away?").lower()
    l7=input("Even ____ I'm away?").lower()
    l8=input("Oti, oti, there's _____ much love when we go OT?").lower()
    l9=input("I pray to make it ____ in one piece?").lower()
    l0=input("I ____, I pray?").lower()
    if (l1=="like" and l2=="your" and l3=="back" and l4=="play" and l5=="not" and l6=="run" and l7 =="when"and l8=="never" and l9==
    "back" and l0=="pray"):
       print("You got that right!you are as cool as me")
       break
    else:
       print("You got that wrong!")
       counter=counter+1
print("Thanks for playing!")
print("You got the correct lyrics in", counter, "attempt(s).")