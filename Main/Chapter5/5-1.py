# OOP > 객체지향 프로그래밍 섹션
# OOP : Object Oriented Programing > 객체지향 프로그래밍
# 직관적이고 데이터와 코드를 잘 구성해줌
# java , typescript python등 주로 사용
# oop는 코드를 구성하는 방법에 대한 규칙이자 실행 방법들에 대한 또다른 방법중하나

#dictionary type
bee = {
    "name" : "Bee",
    "XP" : 1000,
    "team" : "Team X"
}

def create_player_for_team(name, xp, team):
    pass


def create_player(name, xp, team) :
    return {
        "name" : name,
        "XP" : xp,
        "team" : team
    }

def introduct_player(player) : #기능 (요청받음)
    name = player["name"]
    team = player["team"]
    print(f"Hello My name is {name}, and I am {team}.")

introduct_player(bee) #기능 사용 (요청)

#기능과 함수는 딕셔너리는 연결되어있다. 존재할 경우 기능을 사용하고 존재하지않을 경우 사용되지않음.

bee = create_player(name="Bee", xp=1000, team="Team X")
see = create_player(name="Bee", xp=1000, team="Team blue")

teams = {
    "Team X" : [bee],
    "Team blue" : [see]
}
