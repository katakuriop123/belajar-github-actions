import os

def read_file():
    user_input = input("Masukkan nama file: ")
    os.system("cat " + user_input)  # POTENSI COMMAND INJECTION

read_file()
