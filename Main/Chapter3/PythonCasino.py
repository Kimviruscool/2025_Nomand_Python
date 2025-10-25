# UP&Down make

from random import randint
#randint 에서 random 을 호출,설치,수입

#안내문
print("Welcom to UP DOWN GAME")
print(".. ... .. .. choice number in computer")

#변수에 랜덤숫자 입력
pc_choice = randint(1, 100)

#변수에 bool값 True 입력 False가 되면 종료
playing = True

#반복문 playing 변수 호출
while playing:
    user_choice = int(input("Enter your choice : "))
    # 유저가 고른숫자 문자형 > 숫자형 타입변환
    if user_choice == pc_choice: #만약 같으면
        print("You Win!") #안내문 출력
        playing = False # 변수값 변경 = 게임종료
    elif user_choice > pc_choice: # 유저가 고른값이 더 크면
        print("Lower!!") # 낮추라고 안내
    elif user_choice < pc_choice: # 유저가 고른값이 더 작으면
        print("Upper!!") # 높이라고 안내
    else: # 그게 모두 아니면 #필요 없음
        print("system Error replay the game") #시스템 에러 안내 
        playing = False # 변수값 변경 = 게임종료