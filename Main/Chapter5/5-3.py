# Class : class 는 데이터가 어떻게 데이터가 어떻게 생겨야하는지에 대한 청사진

class Dog :
    def __init__(self, name, breed, age):
        self.name = name;
        self.breed = breed;
        self.age = age;

    def sleep(self):
        print("Sleeping zzzzzzzzz")

class GuardDog(Dog) :

    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggresive = True

    def Rrrr (self) :
        print("rrrrr stay away!");



class Puppy(Dog) :

    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1) #super 부모 클래스인 Dog를 참조하는걸 말함

    def woof_woof(self) :
        print("woof woof");


ruffus = Puppy("ruffus", "Beagle") #ruffus는 Puppy의 종류라고 정의
bibi = GuardDog("bibi", "Jindo")

print(bibi, ruffus)

ruffus.woof_woof()

bibi.Rrrr()

bibi.sleep()

# inheritace(상속) 는 우리가 반복하지 않도록 해준다.