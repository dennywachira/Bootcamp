import random

number= random.randint(0,10)
attempts=0
score=0


while attempts <5:
    userNum=int(input("Enter a Number\n"))
    attempts=attempts+1
    if userNum<number:
        print("your guess is too low")
    if userNum>number:
        print("your guess is too high")
    if userNum==number:
        break
if userNum==number:
    score=+1
    print("Congratulations You Won!")
    print("You have Scored:"+"" + str(score)+" "+"points")
    goahead=int(input("Do you wish to Continue Playing? if Yes enter 1,if Not enter 0\n"))
    if goahead==1:
        print("welcome back")
    else:
        print("good bye")
else:
    print(" OOPS!! You lost after"+" " + str(attempts)+" "+ "attempts")

