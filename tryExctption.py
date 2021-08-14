#try,exception,finally,else

num1 = input("Enter a no :")
num2 = input("Enter a no :")
try:                                                                # if try is not working then it jump to the exception
    print("The sum of two numbers is :",int(num1)+int(num2))
except Exception as e:
    print(e)
    print("This line is very important")
else:
    print("Else will run if except is not running")
finally:                                                            # finally is used when we want to run set of code anyway irrespective of try 
    print("Finally should run anyway..")                            # it is also used to close any file which is open (for code cleanup) 

                                                               



# we can also use except this way
# except:
#     print("This line is very important")  
# finally:    
#     print("this should work anyway..")