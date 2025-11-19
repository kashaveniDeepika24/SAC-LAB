'''copy contents of one file into another'''

source_file=input("enter the name of the source file:")
destination_file=input("enter the name of the destination file:")
try:
    with open(source_file,'r') as src:
        content=src.read()
    with open(destinayion_file,'w') as dest:
        dest.write(content)
    print(f"contents of '{source_file}' have been copied to '{destination_file}'")
except FileNotFoundError:
    print("Source file not found. please check the file name and try")
