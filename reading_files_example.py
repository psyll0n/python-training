from sys import argv

try:
    script, filename = argv
    txt = open(filename)

    print(f"Here is your file {filename}:")
    print(txt.read())

    print("Type the filename again:")
    file_again = input(">")
    txt_again = open(file_again)
    print(txt_again.read())
except:
    print("example: python3 reading_files_example.py <textfile_name>")
