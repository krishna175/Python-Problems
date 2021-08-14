# l = 10             # this is a global variable
# def function(n):
#     # l = 4        # this are local variable
#     m = 9          # this are local variable
#     global l       # can change the global value by using the global keyword
#     l = l + 10     # cannot change the value of global variable in local scope
#     print(n,", Good Morning.")
#     print(m,l)

# function("Harikrishnan")
# print(l)
# # print(m):Error =- local vairable cannot be used outside the scope 

x = 7
def hari():
    x = 6
    def rohan():
        global x    
        x = 8 
    print("Before calling rohan :",x)
    rohan()
    print("After calling rohan :",x)
hari()
print(x)