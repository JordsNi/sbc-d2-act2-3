from random import randint

bet1 = int(input("Enter 1st Digit: "))
bet2 = int(input("Enter 2nd Digit: "))
bet3 = int(input("Enter 3rd Digit: "))

print("Your Bet is: ",bet1,bet2,bet3)

r1 = randint(0,9)
r2 = randint(0,9)
r3 = randint(0,9)

print("The Winning Bet is: ",r1,r2,r3)
if bet1 == r1 and bet2 == r2 and bet3 == r3:
    print("You Win!")
elif (bet1 == r1 and bet2 == r3 and bet3 == r2) or (bet1 == r2 and bet2 == r1 and bet3 == r3) or (bet1 == r2 and bet2 == r3 and bet3 == r1) or (bet1 == r3 and bet2 == r1 and bet3 == r2) or (bet1 == r3 and bet2 == r2 and bet3 == r1):
    print("You Partially Win!")
else:
    print("You Lose!")