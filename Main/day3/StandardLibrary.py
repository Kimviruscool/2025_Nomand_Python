# Standar Library

from random import randint
# radom 을 radint 에서 가져오겠다

user_choice = int(input("Enter your choice : \n"))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You win")
elif    user_choice > pc_choice:
    print("Lower Couputer Choice :", pc_choice)
elif user_choice < pc_choice:
    print("Upper Couputer Choice :", pc_choice)
else:
    print("Looser Couputer Choice :", pc_choice)

