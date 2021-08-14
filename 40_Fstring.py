#F STRING
import time # used to check the time took to run the code
seconds = time.time()
me = "hari"
age = 20
marks = 150
total_marks = 200
#1 string formatting (using % opertator)
print("My name is %s "%me)
a = "My name is %s and my age is %s"%(me,age)  #2 ( using tuple)
print(a)

#3 Using (str.format) techinques
b = "My name is {} and my age is {}"
b = b.format(me,age)
print(b)

#4 Using f-string
c = f"My name is {me} and my age is {age} and my percentage is {marks/total_marks*100}% "
print(c)
print(seconds) # used to check the time took to run the code
