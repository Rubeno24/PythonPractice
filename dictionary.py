NBATeams = {
    "Team Name": [
        {"Name": "Lakers", "Players": 
         ["LeBron James", "Anthony Davis", "Russell Westbrook"]},
        {"Name": "Warriors", "Players": 
         ["Stephen Curry", "Klay Thompson", "Draymond Green"]},
        {"Name": "Celtics", "Players": 
         ["Jayson Tatum", "Jaylen Brown", "Marcus Smart"]}
    ]
}


#Prints the whole dictionary
print(NBATeams)

for teams in NBATeams["Team Name"]:
    print(teams["Name"])
