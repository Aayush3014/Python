# 10.	Write a program to define a class Player having variables: name, no of matches played methods: constructor to initialize variable members and display. Define 2 sub-classes Bowler and Batsman that inherit the class Player.
# Class Bowler has variables no of wickets taken, no of overs bowled, no of runs conceded and methods getdata and displayDetail (to display name, matches played, wickets taken, no of overs bowled, no of runs conceded). Class Batsman has variables runs, balls faced and methods getdata and displayDetail (to display name, matches played and strikeRate).
# Define a class AllRounder that inherits the members of Bowler and Batsman class. getdata and displayDetail methods of AllRounder class should use super() method to acess the corresponding methods of Bowler and Batsman classes.


class Player:

    def __init__(self, name, no_of_matches):
        self.name = name
        self.no_of_matches = no_of_matches

    def display(self):
        print("Name : ", self.name)
        print("Matches : ", self.no_of_matches)


class Bowler(Player):

    def __init__(self, name, no_of_matches, no_of_wickets_taken, no_of_overs_bowled):
        Player.__init__(self, name, no_of_matches)
        self.no_of_wickets_taken = no_of_wickets_taken
        self.no_of_overs_bowled = no_of_overs_bowled

    def getdata(self):
        Player.display(self)

    def display(self):
        print(
            f"Wickets taken : {self.no_of_wickets_taken} \nNo. of overs bowled : {self.no_of_overs_bowled}")


class Batsman(Player):

    def __init__(self, name, no_of_matches, runs, balls_faced):
        Player.__init__(self, name, no_of_matches)
        self.runs = runs
        self.balls_faced = balls_faced

    def getdata(self):
        Player.display(self)

    def displaydetail(self):
        print("Runs : ", self.runs)
        print("Balls faced : ", self.balls_faced)


class Allrounder(Bowler, Batsman):

    def __init__(self, name, no_of_matches, no_of_wickets_taken, no_of_overs_bowled):
        super(Allrounder, self).__init__(name, no_of_matches,
                                         no_of_wickets_taken, no_of_overs_bowled)
        print(f"Name : {self.name} \nMatches played : {self.no_of_matches}")


print("-------------------------------------------")
print("<<<<<-------------Bowler---------->>>>>>")
A1 = Bowler("john", 40, 54, 2)
A1.getdata()
A1.display()
print("<<<<<-------------Batsman---------->>>>>>")
A2 = Batsman("Rohan", 65, 78, 5)
A2.getdata()
A2.displaydetail()
print("<<<<<-------------Allrounder---------->>>>>>")
A3 = Allrounder("Naruto", 91, 3, 82)
print("-------------------------------------------")
