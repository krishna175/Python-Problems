numbers = ["11","2","32","43","23"]

# for item in numbers:
#     item = int(item)
#     print(item+1)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

 # the map function converts all the elements in the numbers list into integer we save that in list format
numbers = list(map(int,numbers))  # for map function map(datatype which we want to convert,name or variable where values are stored)
                                    #map(function,itrable)

numbers2 = numbers[2] + 8
print(numbers2)

#converting each integer element in the list into string
string = [4,64,6,54,2]

string = list(map(str,string))
print (string)


# def sqr(a):
#     return a*a

square = [4,64,6,54,2,3,23,9]
square = list(map(lambda a: a*a, square))
print(square)


def sq(a):
    return a*a

def cube(a):
    return a*a*a

func = [sq,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

print("---------------------FILTERS---------------------")
list1 = [1,2,3,4,5,6,7,8,9,0]
def is_greater_5(num):
    return num>5

# print(is_greater_5(7))
gr_than_5 = list(filter(is_greater_5,list1)) # in filters (the name of function,and the place where we wnat to apply filter)
print(gr_than_5)

print("---------------------REDUCE------------------")
from functools import reduce
list = [1,2,3,4,5,9]
# num = 0
# for i in list:
#     num = num+i
# print(num)

#we can do this using reduce function
num = reduce(lambda x,y:x+y,list)
print(num)






