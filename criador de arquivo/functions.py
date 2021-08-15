#file_name: str, file_extension: str = ".txt"
#file_name: str, file_extension: str = ".txt", file_content: str = ""
import os

def create():
    file_name = str(input("File name: "))
    file_extension = str(input("File extention: "))
    file = open(f"{file_name}{file_extension}", "x")

def write():
    file_name = str(input("File name: "))
    file_extension = str(input("File extention: "))
    file_content = str(input("File content: "))
    with open(f"{file_name}{file_extension}", "w") as file:
        content = file.write(file_content)

def append():
    file_name = str(input("File name: "))
    file_extension = str(input("File extention: "))
    file_content = str(input("File content: "))
    with open(f"{file_name}{file_extension}", "a") as file:
        content = file.write(file_content)

def read():
    file_name = str(input("File name: "))
    file_extension = str(input("File extention: "))
    with open(f"{file_name}{file_extension}", "r") as file:
        print(file.read())

def delete():
    file_name = str(input("File name: "))
    file_extension = str(input("File extention: "))
    if os.path.exists(f"{file_name}{file_extension}"):
        os.remove(f"{file_name}{file_extension}")
    else:
        print("The file does not exist")