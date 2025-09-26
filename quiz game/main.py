print("Welcome to computer quiz !.")

playing=input("Do you want to play ?.").lower().strip()

if playing != 'yes':
    quit()

print("Ok lets play !.")

answer=input("What does CPU stands for ?..").lower().strip()
if answer=='central processing unit':
    print("Correct")
else:
    print("wrong")

answer=input("What does GPU stands for ?..").lower().strip()
if answer=='graphics processing unit':
    print("Correct")
else:
    print("wrong")

answer=input("What does RAM stands for ?..").lower().strip()
if answer=='random access memory':
    print("Correct")
else:
    print("wrong")

answer=input("What does PSU stands for ?..").lower().strip()
if answer=='power supply unit':
    print("Correct")
else:
    print("wrong")