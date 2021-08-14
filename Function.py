a = 19 
b = 4
c = sum((a,b)) # predefind function 
print(c)

def function1():
    print("You are in function 1")
function1()
                                                                                                                                       
def function2(a,b):
    print("the sum is ",a+b)
function2(1,4)

def function3(a,b):
    """This is a function to calculate the average of 2 given numbers """  # this is docstring # helps the dev to know what is the use of this function
    avg = (a+b)/2
    # print(avg)
    return avg
x = function3(2,4)
# print(x)
print(function3(2,4))
print(function3.__doc__)
# print(sum.__doc__)





