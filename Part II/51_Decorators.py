def function1():
    print("Good Morning")

func2 = function1
del function1               # here if we delete the function1 then also it is printed because it is now stored in func2
func2()


# returning function inside a function
def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(0)
print(a)

# pass function in a function as an argument

def executer(func):
    func("this")
executer(print)


print("----------DECORATOR------------")

def dec1(func1):
    def executer():
        print("Executing Now")
        func1()
        print("Execution Completed")
    return executer

@dec1
def myName():
    print("My Name is HARIKRISHNAN SATHYAN")

# myName = dec1(myName)  insted of writing this line we are writing @dec1
myName()

# here we are passing a function inside another function as an argument