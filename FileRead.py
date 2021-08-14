f = open("hari.txt" , "rt")   # here read and text mode are default if we not write then also it will give the same output
print(f.readlines())          # to get lines in the form of list

# print(f.readline())         # it reads a single line
# print(f.readline())         # now it includes the next line
# print(f.readline())
# for line in f:
#     print(line ,end = "")   # to print each line by line from the file

# content = f.read()
# print(content)
# content = f.read(3)  # if I want to read first 3 character from the file
# print(content)
# f.close()            # we should always close a file if we open it
    