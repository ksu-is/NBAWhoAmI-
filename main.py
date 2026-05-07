import random
print("Welcome to NBA Who Am I - Guess the player!")

players = {
    "LeBron James": [
        "Played for the Cavaliers and Lakers",
        "Multiple NBA championships",
        "Known as King James"
    ],
    "Stephen Curry": [
        "Elite three-point shooter",
        "Star for Golden State Warriors",
        "Multiple MVP awards"
    ],
    "Giannis Antetokounmpo": [
        "Known as the Greek Freak",
        "Milwaukee Bucks superstar",
        "NBA MVP and Finals MVP"
    ],
    "Jayson Tatum": [
        "Star forward for the Boston Celtics",
        "Key player in NBA Finals runs",
        "Elite scorer and two-way player"
    ],
    "Nikola Jokić": [
        "Center for the Denver Nuggets",
        "Multiple MVP awards",
        "Elite passing big man"
    ],
    "Anthony Edwards": [
        "Explosive guard for the Minnesota Timberwolves",
        "Known for athletic scoring ability",
        "One of the league’s rising young stars"
    ],
    "Shai Gilgeous-Alexander": [
        "Star guard for the Oklahoma City Thunder",
        "Elite scorer and playmaker",
        "One of the NBA’s top young MVP-level players"
    ],
    "Kevin Durant": [
         "Elite scorer",
         "Won multiple NBA championships",
         "Played for Warriors and Suns"
 ]
}

player = random.choice(list(players.keys()))

print("NBA Who Am I?")

for clue in players[player]:
    print("Clue:", clue)
    guess = input("Your guess: ")

    if guess.lower() == player.lower():
        print("Correct!")
        break
else:
    print("The answer was:", player)