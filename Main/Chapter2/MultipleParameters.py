#Multiple parameters

#다중 파라미터

def say_hello(user_name, user_age):
    print("Hello", user_name);
    print("you are", user_age, "years old");

#say_hello("bee") #()(괄호)는 실행버튼, 데이터를 보내는 곳
# 실행시 user_age의 값을 argumenet 하지않아서 실패

say_hello("bee", 12)
# first argument "bee" / second argument 12

print("hello world")

# 몇개의 argument를 사용할 수 있는가?
# def의 parameters를 정의한만큼 (first/second)
# print function 의 경우 * 을 사용한 무한대 값을 사용가능