from random import randint

P1 = input("Choose Fold or Unfold: ")
print("P1 picks", P1)

C2 = randint(1,2)
if C2 == 1:
    print("C2 picks Fold")
else:
    print("C2 picks Unfold")

C3 = randint(1,2)
if C3 == 1:
    print("C3 picks Fold")
else:
    print("C3 picks Unfold")

if P1 == "Fold" and C2 == 2 and C3 == 2:
    print("Player 1 Wins!")
elif P1 == "Unfold" and C2 == 1 and C3 == 2:
    print("Computer 2 Wins!")
elif P1 == "Unfold" and C2 == 2 and C3 == 1:
    print("Computer 3 Wins!")
elif P1 == "Unfold" and C2 == 1 and C3 == 1:
    print("Player 1 Wins!")
elif P1 == "Fold" and C2 == 2 and C3 ==1:
    print("Computer 2 Wins!")
elif P1 == "Fold" and C2 == 1 and C3 == 2:
    print("Computer 3 Wins!")
elif P1 == "Fold" and C2 == 1 and C3 == 1:
    print("Draw!")
elif P1 == "Unfold" and C2 == 2 and C3 == 2:
    print("Draw!")
else:
    print("Invalid Match!")