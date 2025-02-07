class Player:
    def __init__(self,name,id,position):
        self.name = name
        self.id = id
        self.position = position
        self.goals_scored = 0
        self.assists = 0
        self.yellow_card = 0
        self.red_card = 0

    def scoreAGoal(self):
        self.goals_scored +=1

    def makeAnAssit(self):
        self.assists +=1

    def receiveAYellowCard(self):
        self.yellow_card +=1

    def receiveARedCard(self):
        self.red_card +=1

    def printStats(self):
        return f"""
ID         : {self.id}
Nom        : {self.name}
Position   : {self.position}
Goals       : {self.goals_scored}
Assits     : {self.assists}
Yellow cards : {self.yellow_card}
Red cards : {self.red_card}"""

class Team:
    def __init__(self,name_team):
        self.name_team = name_team
        self.player_list = []

    def addPlayer(self, player : Player):
        self.player_list.append(player)

    def printStatsTeamPlayer(self):
        print(f"Team : {self.name_team}")
        for player in self.player_list:
            print(player.printStats())

    def updateStatsPlayer(self,numero,action):
        for player in self.player_list:
            if player.id == numero:
                if action == "goal":
                    player.scoreAGoal()
                elif action == "pass":
                    player.makeAnAssit()
                elif action == "yellow":
                    player.receiveAYellowCard()
                elif action == "red":
                    player.receiveARedCard()


ronaldo = Player("ronaldo",7,"ATK")
bebere = Player("bebere",10,"MID")
jean_louis = Player("Jean-louis",2,"DEF")

palmier_FC = Team("Palmier_FC")
palmier_FC.addPlayer(ronaldo)
palmier_FC.printStatsTeamPlayer()

the_bests = Team("The Bests")
the_bests.addPlayer(bebere)
the_bests.addPlayer(jean_louis)
the_bests.printStatsTeamPlayer()

print("match start !")

palmier_FC.updateStatsPlayer(7,"goal")
the_bests.updateStatsPlayer(10,"yellow")
the_bests.updateStatsPlayer(10,"pass")
the_bests.updateStatsPlayer(2,"goal")
palmier_FC.updateStatsPlayer(7,"red")

print("match finish !!!!")

palmier_FC.printStatsTeamPlayer()
the_bests.printStatsTeamPlayer()