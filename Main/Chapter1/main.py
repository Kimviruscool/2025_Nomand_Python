a = 2
b = 3
c = a + b
#파이썬은 코드를 위에서 아래로 읽는다

a = 1
b = 10
# 위에 코드가 변해도 차례대로 읽기때문에 값은 변하지 않는다.
print(c)

#Variable #변수

my_age = 88 #_ , Camel Case 등 방법은 사용가능하지만 공백,시작이숫자 은(는) 불가능하다.


#data type

#int #숫자는 기본적으로 int
my_age = 77

#String #문자열
my_name = "Nico" #String type 문자열
#문자열은 "" 큰따옴표로 감싸서 문자열로 만든다
my_name2 = "12" #큰따옴표로 감싸면 모두 문자가된다
print(my_name)
print(my_name2)

#boolean #불리언 #True참 , False거짓 만 출력가능
my_answer = True
my_answer2 = False
print(my_answer)
print(my_answer2)
#"" 를 사용하면 Boolean 타입이 아니라 String 타입으로 적용된다.

print("Hello my name is", my_name)
print("and I'm ", my_age, "years old")