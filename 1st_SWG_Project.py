import random                                                                    #Created By, Pralay Das
                                                                                 #Date : 23/12/2020
def Roll_of_game(computer, user):
    if computer == user:
        return None
    elif computer == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True
    elif computer == 'w':
        if user == 's':
            return True
        elif user == 'g':
            return False
    elif computer == 'g':
        if user == 'w':
            return True
        elif user == 's':
            return False
    else:
        pass

name = input("Enter Your Name: ")

randNo = random.randint(1, 3)
print("Computer - Snake (S), Water (W), Gun (G) : ")

if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'

user = input("User - Snake (S), Water (W), Gun (G) : ")
print(f"Computer : {computer}")
print(f"User : {user}")
u = Roll_of_game(computer, user)
if u == None:
    print("Game is Tie!")
elif u:
    print("You Wine..)")
else:
    print("You Lose..!")

print("Thank You ", name, "for Playing this Game!")



