import random

number= random.randint(0,10)
attempts=0
score=10
print("WELCOME to our guessing Game!\nYou will guess a number between (0 and 10),if it's correct you win and if its wrong we offer you 5 attempts.")
print("Lets start playing!!!!")

while attempts <5:
    userNum=int(input("Guess a Number\n"))
    attempts=attempts+1
    if userNum<number:
        print("your guess is too low try a higher Number")
        score=score-1
        print("You have: "+ str(score)+"points")
    if userNum>number:
        print("your guess is too high try a lower number")
        score=score-1
        print("You have: "+ str(score)+"points")
    if userNum==number:
        break
if userNum==number:
    score=score+5
    print("Congratulations You Won!")
    print("You have Scored:"+"" + str(score)+" "+"points")
    
else:
    print(" OOPS!! You lost after"+" " + str(attempts)+" "+ "attempts")

