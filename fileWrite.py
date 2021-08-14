# f = open("hari2.txt","w")  
# f.write("hari2 is a good boy")  # this will replace the file contect with this text 
# f.close()                       # and if the file is not present then it will create file with that particular name

# f = open("hari.txt","a")        # it appends or adds the text into the file at the end without change the previous content 
# a = f.write("\nRamesh is also a bad boy")  
# print(a)                        # this will give the no of appended character
# f.close()                       

# Read and Write mode.

f = open("hari2.txt","r+") 
print(f.read())
f.write("Rahul is a good boy")
f.close()
