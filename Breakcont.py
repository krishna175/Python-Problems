'''Program to ask for input greater than 100 until the user enter a no greater than 100'''

n=int(input("Pls enter no : "))
while(True):
    if n<100:
        n=int(input("Try again!!! \n Pls enter a no : "))
        continue
    elif n>=100:
        print("Now you are right")
        break
        print(n)
       

'''Alternate solution'''
# while(True):
#     n=int(input("Enter a number :  "))
#     if n<100:
#         print("Sorry please try again!!!")
#         break
#     else:
#         print("Your input is right")
#         continue
