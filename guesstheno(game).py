n=18
g=1
print("You have only 5 attempts")
while(g<=5):
    print("Attempt no",g,"\n")
    x=int(input("Guess the number :"))
    if g==5 and n!=x:
        print("GAME OVER!!\nThe correct answer was: 18")
        break
    elif x>n:
        print(x,": is greater than the original number\nTry a number less than :",x,"\n" )
    elif x<n:
        print(x,"is lesser then the original no\nTry a number greater than :",x,"\n")  
    elif x==n:
        print("Congrats!!! ",x,"is the right answer \n") 
        break 
    g+=1 
        
 