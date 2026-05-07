import random

players = {
    "LeBron James": [
        "Played for the Cavaliers",
        "Won multiple NBA championships",
        "Known as King James"
    ],
    "Stephen Curry": [
        "Great three-point shooter",
        "Played for Golden State",
        "Won MVP awards"
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
    