name = "Harikrishnan"

def printjoke(str):
    print(f"This is a joke {str}")

printjoke(name)
print("This is my working direcrory",__name__)  # here in file2 the name is equal to main but in case of file1 the name will be equal to file2 i.e the name of the file
if __name__ == '__main__':              # this will not be executed while exporting to another file
    print("my name is hari")
    print("I'am doing python")