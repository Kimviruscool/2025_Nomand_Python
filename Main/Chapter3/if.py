#if / 조건문

if 10 > 5 :
    print("true")

a = "bee"

if a == "bee" :
    print("Yeah He's bee")

password = False
if password : #만약 ~~하면
    print("Here is your money")
else: #그렇지않다면
    print("Wrong password")

winner = 10
if winner > 10:
    print("Winner is greater than 10")
elif winner < 10 :
    print("Winner is less than 10")
else:
    print("Winner is 10")

#if 문 조건이 True 일때만 걸린다 python은 위에서 아래로 코드를 읽기때문에 하나라도 걸리면 그것을 반환한다.
