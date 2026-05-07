import tkinter as tk
import random

players = {
    "LeBron James": [
        "Played for Cavaliers and Lakers",
        "NBA champion and MVP",
        "Known as King James"
    ],
    "Stephen Curry": [
        "Best shooter in NBA history",
        "Golden State Warriors star",
        "Multiple MVP awards"
    ],
    "Giannis Antetokounmpo": [
        "Known as the Greek Freak",
        "Milwaukee Bucks superstar",
        "NBA champion and MVP"
    ],
    "Nikola Jokić": [
        "Denver Nuggets center",
        "Elite passing big man",
        "Multiple MVP awards"
    ],
    "Jayson Tatum": [
        "Boston Celtics star forward",
        "Elite scorer and two-way player",
        "Key NBA Finals performer"
    ],
    "Anthony Edwards": [
        "Explosive guard for Timberwolves",
        "Elite athletic scorer",
        "Rising NBA superstar"
    ],
    "Shai Gilgeous-Alexander": [
        "Oklahoma City Thunder star guard",
        "Elite midrange scorer",
        "MVP-level performance in recent seasons"
    ],
    "Kevin Durant": [
        "One of the greatest scorers ever",
        "NBA champion and MVP",
        "Plays forward position"
    ],
    "Luka Dončić": [
        "Elite playmaking guard/forward",
        "Known for step-back shots and scoring",
        "One of the NBA’s top young stars"
    ],
    "Joel Embiid": [
        "Dominant center for the 76ers",
        "NBA MVP",
        "Elite scoring big man"
    ],
    "Damian Lillard": [
        "Elite deep-range shooter",
        "Known as 'Dame Time'",
        "All-NBA point guard"
    ],
    "Kawhi Leonard": [
        "Two-time NBA champion",
        "Elite defensive player",
        "Known for clutch playoff performances"
    ],
    "Devin Booker": [
        "Star shooting guard for the Suns",
        "Elite scorer",
        "NBA Finals appearance"
    ],
    "Donovan Mitchell": [
        "Explosive scoring guard",
        "Star for Cleveland Cavaliers",
        "Known for high-scoring games"
    ],
    "Bam Adebayo": [
        "Defensive anchor for Miami Heat",
        "Elite versatile big man",
        "NBA Finals competitor"
    ]
}

# Pick random player
player = random.choice(list(players.keys()))
clues = players[player]
clue_index = 0

# Create window
root = tk.Tk()
root.title("NBA Who Am I Game")
root.geometry("500x420")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="🏀 NBA WHO AM I 🏀",
    font=("Helvetica", 18, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=10)

# Clue display
clue_label = tk.Label(
    root,
    text="Click 'Next Clue' to start!",
    font=("Helvetica", 14),
    fg="yellow",
    bg="#1e1e2f",
    wraplength=400
)
clue_label.pack(pady=20)

# Input box
guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#1e1e2f")
result_label.pack(pady=10)

# Functions
def next_clue():
    global clue_index
    if clue_index < len(clues):
        clue_label.config(text="Clue: " + clues[clue_index])
        clue_index += 1
    else:
        clue_label.config(text="No more clues!")

def check_guess():
    guess = guess_entry.get()
    if guess.lower() == player.lower():
        result_label.config(text="Correct! 🎉", fg="green")
    else:
        result_label.config(text="Try again!", fg="red")

# Buttons
tk.Button(
    root,
    text="Next Clue",
    command=next_clue,
    bg="#4A90E2",
    fg="white",
    activebackground="#357ABD",
    activeforeground="white",
    font=("Helvetica", 12, "bold"),
    relief="flat",
    padx=10,
    pady=5
).pack(pady=5)

tk.Button(
    root,
    text="Submit Guess",
    command=check_guess,
    bg="#2ECC71",
    fg="white",
    activebackground="#27AE60",
    activeforeground="white",
    font=("Helvetica", 12, "bold"),
    relief="flat",
    padx=10,
    pady=5
).pack(pady=5)

root.mainloop()