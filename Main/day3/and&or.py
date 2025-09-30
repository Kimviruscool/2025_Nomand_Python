# And & Or

age = input("How old are you?\n")
# \n 줄바꿈

print(type(age))
#type 은 변수,함수의 타입을 확인하는 기능

age = int(age) #타입 변환
print(type(age))

if age < 18 :
    print("You are young")
elif age >=18 and age <= 35 :
    print("You can drink beer!")
elif age == 60 or age == 70 :
    print("Wow old man!")
else:
    print("You are older")

# AND
# TRUE AND TRUE = TRUE
# TURE AND FALSE = FALSE
# FALSE AND TRUE = FALSE
# FALSE AND FALSE = FALSE

# OR
# TRUE OR TURE = TRUE
# TURE OR FALSE = TRUE
# FALSE OR TURE = TRUE
# FALSE OR FALSE = FALSE