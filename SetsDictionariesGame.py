def makePacificDivision():
    pacific = {
        "Golden Knights": {"W": 16, "L": 5, "OTL": 6},
        "Canucks": {"W": 17, "L": 9, "OTL": 2},
        "Kings": {"W": 15, "L": 9, "OTL": 4},
        "Oilers": {"W": 13, "L": 12, "OTL": 1},
        "Kraken": {"W": 8, "L": 13, "OTL": 7},
        "Flames": {"W": 11, "L": 14, "OTL": 3},
        "Ducks": {"W": 10, "L": 17, "OTL": 0},
        "Sharks": {"W": 8, "L": 17, "OTL": 3}
    }
    return pacific

def calculateStats(teams):
    for team in teams:
        w = teams[team]["W"]
        l = teams[team]["L"]
        otl = teams[team]["OTL"]
        games = w + l + otl
        points = (2 * w) + otl
        teams[team]["GP"] = games
        teams[team]["PTS"] = points
    return teams

def printStandings(teams):
    print("PACIFIC DIVISION STANDINGS")
    print("---------------------------------------------")
    print("Team                 GP   W   L  OTL  PTS")
    print("---------------------------------------------")
    for team, data in teams.items():
        print(f"{team:<20} {data['GP']:>2}  {data['W']:>2}  {data['L']:>2}  {data['OTL']:>3}  {data['PTS']:>3}")

def main():
    teams = makePacificDivision()
    teams = calculateStats(teams)
    printStandings(teams)

main()