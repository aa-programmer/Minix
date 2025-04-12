import re
import os

def a(filename):
    print("\n\nMinix v0.1.0\n\n")

    with open(filename, "r") as file:
        content = file.read()
        content = "import random\n" + content
        content = re.sub(r'\bfunc\b', 'def', content)
        content = re.sub(r'\blog\b', 'print', content)
        content = re.sub(r'\bstring\b', 'str', content)
        content = re.sub(r'\binteger\b', 'int', content)
        content = re.sub(r'\bret\b', 'return', content)
        content = re.sub(r'\brand_integer\b', 'random.randint', content)
        content = re.sub(r'\brand_string\b', 'random.choice', content)
        exec(content)

    print("\n\nCode Executed.\n\n")

filename = input("Enter the File Name: ")
if not filename.endswith(".mx"): filename += ".mx"
if os.path.exists(filename): a()
else: raise FileNotFoundError("File does not Exists, Check the Spelling and Make sure it is in the EXE is in the right directory.")