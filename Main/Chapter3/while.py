# while / 반복문

from random import randint
# radom 을 radint 에서 가져오겠다
'''
주석처리되는 부분
'''


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

#무한 반복문
# while True :
#     print("Hello")

#조건 반복문
distance = 0
while distance <= 20:
    print("Distance :", distance, "Km")
    distance = distance + 1