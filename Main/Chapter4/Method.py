# data structure 자료구조
# list , tuple , dictionary
# List = [] 대괄호 안에 넣는방법 값이 변할 수 있다
# tuple = (9,8,7,6,5) ,를 사용하여 추가하고 값이 변할 수 없다
#dictionary = {"name" = "bee"} 와 같이 사용되며 key = value , 키 = 값 으로 정의 수정가능

#1
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"
sat = "Sat"
sun = "Sun"
print(mon);
print("");
print("");

#2
aweek = "Mon,Tue,Wed,Thu,Fri,Sat,Sun"
print(aweek);
print("");
print("");

#3 List []
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(week);
print(week[0]);
print("");
print("");

#4 tuple ()
week2 = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
print(week2);
print(week[0]);
print("");
print("");

#5 dictionary {}
week3 = {
    1 : "Mon",
    2 : "Tue",
    3 : "Wed",
    4 : "Thu",
    5 : "Fri",
    6 : "Sat",
    7 : "Sun"
}
print(week3);
print(week3[1]);
print("");
print("");

name = "bee"

print(name.replace("bee","boo"));
#.upper() 대문자로 변경해주기
#.capitalize() 첫글자만 대문자로 변경해주기
#.split() 자르기
#starswith("조건") 맨앞에 조건이 들어가있는지 true/false
#endswith("조건") 맨뒤에 조건이 들어가있는지 true/false
#replace("현재데이터", "변경할데이터") 데이터변경

#method는 데이터에 결합된 function이다.
print("");
print("");

#List
print(week.count("Mon")); #Mon이 몇개있는지

week.append("End Week"); #리스트에 추가하기
print(week);

week.remove("End Week"); #리스트에서 제거하기
print(week);

week.reverse(); #순서 뒤집기
print(week);

week.clear() #clear 하기
print(week);

#dic
player = {
    'name' : 'bee',
    'age' : 22,
    'gender' : 'male',
    'alive' : True,
    'favFood' : ["🍎","🍔"]
}

print(player);
print(player.get('name'));
print(player.get('favFood'));
print(player['favFood'][1]);
player.pop('gender'); # DIC 지우기
print(player);
player['xp'] = 15000;
print(player);
player['favFood'].append("🥚");
print(player['favFood']);