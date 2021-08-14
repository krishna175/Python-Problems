import random
l1 = ["ROCK","PAPER","SCISSORS"]
# human_val = input("R-Rock\nP-Paper\nS-Scissor\nGive your input : ")
play_limit = 0
human_point = 0
computer_point = 0

while (play_limit<10):
    computer_val = random.choice(l1)
    human_val = input(F"Round {play_limit+1}\nR-Rock\nP-Paper\nS-Scissor\nGive your input : ")
    if(computer_val=="ROCK"and human_val=="R" or computer_val=="PAPER" and human_val=="P" or computer_val=="SCISSORS" and human_val=="S"):
        print(f"The computer input was {computer_val} and you input was {human_val} ")
        print("Tie Game")

    elif(human_val=="P" and computer_val=="ROCK" or human_val=="R" and computer_val=="SCISSORS" or human_val=="S" and computer_val=="PAPER" ):
        print(f"The computer input was {computer_val} and you input was {human_val} ")
        print("You win!")
        human_point +=1
    elif(computer_val=="PAPER" and human_val=="R" or computer_val=="SCISSORS" and human_val=="P" or computer_val=="ROCK" and human_val=="S"):
        print(f"The computer input was {computer_val} and you input was {human_val} ")
        print("You lost!")
        computer_point+=1
    else:
        print("Wrong input!")
    play_limit+=1
    print(f"YOUR POINT: {human_point} & COMPUTER POINT : {computer_point}")
    print("-------------------------------------------------------------\n")
    if play_limit==9:
        print("            ------|LAST ROUND|------")
print("GAME OVER")
if(computer_point==human_point):
    print("This game was a tie")
    print(f"TOTAL SCORE\n===================================\nCOMPUTER: {computer_point} | YOUR POINT: {human_point}")
elif(computer_point>human_point):
    print("Computer won the game")
    print(f"TOTAL SCORE\n===================================\nCOMPUTER: {computer_point} | YOUR POINT: {human_point}")

else:
    print("Congrats! YOU WON")
    print(f"TOTAL SCORE\n===================================\nCOMPUTER: {computer_point} | YOUR POINT: {human_point}")
