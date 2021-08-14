# f = open("hari.txt")
# print(f.read())
# f.close()

#  we can also do the same thing by with block
#     without writing f=open.... and f.close...

with open("hari.txt","r") as f:
    print(f.seek(20))
    print(f.readline())
    # print(f.readlines())

    print(f.read())