#function / def

#print는기본적으로 제공되는 def/function 중 하나로 콘솔에 출력하는 기능
#print(True) #boolean type #bool type
#print("hello") #String type
#print(12) #int type
print(True, "hello", 12) #,(콤마사용으로 bool,String,int 타입 사용)

# #def(정의하다) = function(기능)
# def say_hello(): #공백,숫자로는 불가능하다. #def 정의
#     #def 다음 들여쓰기가 있는이유?
#     #sapce2 , tab을 사용해서 def 안에 코드가 포함되어있음을 정의
#     print("Hello how are you?");

# def say_bye():
#     print("Bye!")

# say_hello() #def호출
# def()에서 ()는 실행버튼

#parameters : 파라미터란 정의한 def/function 에서 받는 값
#출력 결과를 변경하기위에 데이터보내기
#과제 1 : hello username how r u?로 데이터바꾸기

def say_hello(user_name): #user_name : parameters
    print("Hello", user_name, "how r u?");

# say_hello() #보낼 데이터가 없기때문에 오류발생

say_hello("byeong")#데이터를 보냈기때문에 작동
# argument : def/function (으)로 전달한 data(현재코드에서는 "byeong"(String) )
# say_hello("lyn")

#print def 에서는 ,(콤마) 가 사용 가능하다.