from functions import *

commands = ("X", "W", "A", "R", "D")

print("Select the command:\n[X] = Create\n[W] = Write\n[A] = Append\n[R] = Read\n[D] = Delete")

user = str(input("Your command: ")).upper()

if user == "X":
    create()
elif user == "W":
    write()
elif user == "A":
    append()
elif user == "R":
    read()
elif user == "D":
    delete()
else:
    print("Error")