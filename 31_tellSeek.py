f = open("hari.txt","r")
# print(f.tell())           # to know the index of the file pointer
print(f.readline()) 
# print(f.tell())
print(f.readline()) 
# print(f.tell())
# print(f.seek(0))            # to set pointer to the desired place
print(f.readline()) 
f.close()
