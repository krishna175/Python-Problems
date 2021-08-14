l1 = ["Apple","Orange","Grapes","Banana","Mango","Pinapple","Pappaya"]
#t1 = ("Apple","Orange","Grapes","Banana","Mango","Pinapple","Pappaya")

i = 1
for item in l1:
    if (i%2!=0) :
        print(f"Buy {item}",i)
    i+=1

# This can be done using the enumerate fuction
print("---------ENUMERATE-----------")

for index, item in enumerate(l1): # we can also loop through string,tuple,object
    if index%2==0:
        print(f"Buy {item}",index)

# we can change the start index of the enumerate funcion
# here the index will start form 3 and not 0
result = enumerate(l1, 3)
print(list(result))


#-----------ENUMERATE FUNCITON------------------

#A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
# Python eases the programmers’ task by providing a built-in function enumerate() for this task.
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of
# tuples using list() method.
