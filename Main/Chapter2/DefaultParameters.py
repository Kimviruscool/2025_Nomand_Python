#default Parameter

def say_hello(user_name="anonymous"):
    print("Hello", user_name)

say_hello("bee")

# 이름이 없는경우 익명에게 인사하는 방법
say_hello()
# user_name="anonymous" 기본 값을 설정 해준다
# arguments 받지 않지만 기본값으로 anonymous 가 적용되어있기때문에 실행이가능하다.

#calculrator 계산기 만들기
def plus(a , b): #더하기
    print ("PLUS ANSWER :",a + b)

plus(1,2)

def minus(a , b): #빼기
    print("MINUS ANSWER :",a - b)

minus(2,1)

def multiply(a , b): #곱하기
    print("MULTIPLY ANSWER : ",a * b)

multiply(2,2)

def divide(a , b): #나누기
    print("DIVIDE ANSWER : ",a / b)

divide(6,2)

def power(a, b): #제곱
    print("POWER ANSWER : ",a ** b)

power(2,2)