# Class : class 는 데이터가 어떻게 데이터가 어떻게 생겨야하는지에 대한 청사진

class Puppy :

    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"{self.breed} Puppy name : {self.name}\n"

ruffus = Puppy("ruffus", "Beagle") #ruffus는 Puppy의 종류라고 정의
bibi = Puppy("bibi", "Jindo")

print(bibi, ruffus)

# print(ruffus)
# 결과 : <__main__.Puppy object at 0x000002A852EE7F10>
# ruffus 는 puppy의 객체임을 알려줌

#method는 class안에 함수
# class 밖에 있으면 함수 function class 안에 있으면 method

# 규칙
# 메소드는 클래스 안의 기능이다
# 메소드를 가지고있을경우 메소드의 첫번째는 어떤 메소드인지 상관없이 클래스안에있다면 argument(반환받는값은) self여야한다.
# 클래스 안에 모든 첫번째 method 는 자기자신 argument 에서 참조받고있다
# python은 __init__ method를 자동으로 부름으로써  커스텀 가능하게 한다.
# 구조상 dictionary와 비슷해보이지만 다름
# class를 사용할때 함수사용과 똑같이 ()syntax 소괄호를 사용 해야함
# 여럿 arguments(받는값을 이용해서 custom 가능)