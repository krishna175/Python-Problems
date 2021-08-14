# Lambda function or anonymous function
def add(a,b):
    return a+b

#we can also write this function using anonymous function

add = lambda a,b :  a+b

print(add(2,5))

def a_first(a):
    return a[1]
    
a = [[1,7],[2,3],[94,5]]

a.sort(key=a_first)
print(a)