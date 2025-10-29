#code challenge

class Player :
    def __init__(self, name, team) :
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello I'm {self.name} and I play for {self.team}")

class Team :
    def __init__(self, team_name) :
        self.name = team_name
        self.players = []

    def show_players(self) :
        for player in self.players :
            player.introduce()

    def add_player(self, name) :
        new_player = Player(name, self.name)
        self.players.append(new_player)

team_x = Team("X")
team_x.add_player( "bee")

team_y = Team("Y")
team_y.add_player( "Lynn")

team_x.show_players()
team_y.show_players()