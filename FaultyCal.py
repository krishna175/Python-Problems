'''
Calculations to do wrong with.
45 x 3 = 555
56 + 9 = 77
56 / 6 = 4
'''
x=int(input("Enter the 1st no :"))
y=int(input("Enter the 2nd no :"))
r=input("select any one operator no:\n(1) add\n(2) sub\n(3) mul\n(4) dev\n:" )
a=x+y
b=x-y
c=x*y
d=x/y   
if r=="+":
    if  x==56 and y==9:
        print(x,"+",y,"=",77)
    else:    
        print(x,"+",y,"=",a)
elif r=="-":
    print(b)
elif r=="*":
    if  x==45 and y==3:
        print(x,"*",y,"=",555)
    else:    
        print(x,"*",y,"=",c)
elif r=="/":
    if x==56 and y==6:
        print(x,"/",y,"=",4)
    else:
        print(x,"/",y,"=",d) 
else:
    print("Sorry wrong input!!")                   