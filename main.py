import tkinter as tk
import random

players = {
    "LeBron James": [
        "Known as King James",
        "One of the greatest players ever",
        "Multiple-time NBA champion and MVP"
    ],

    "Stephen Curry": [
        "Greatest shooter in NBA history",
        "Changed basketball with deep threes",
        "Multiple-time MVP"
    ],

    "Giannis Antetokounmpo": [
        "Known as the Greek Freak",
        "Dominant two-way superstar",
        "NBA champion and MVP"
    ],

    "Nikola Jokić": [
        "Elite passing center",
        "Multiple-time MVP",
        "Known for incredible basketball IQ"
    ],

    "Jayson Tatum": [
        "Elite scoring forward",
        "Regular All-Star selection",
        "Known for smooth offensive game"
    ],

    "Anthony Edwards": [
        "Explosive athlete",
        "Known for highlight dunks",
        "One of the NBA’s rising superstars"
    ],

    "Shai Gilgeous-Alexander": [
        "Elite midrange scorer",
        "Crafty offensive player",
        "MVP-level talent"
    ],

    "Kevin Durant": [
        "One of the greatest scorers ever",
        "Very tall for his position",
        "NBA champion and MVP"
    ],

    "Luka Dončić": [
        "Elite playmaker and scorer",
        "Known for step-back shots",
        "International superstar"
    ],

    "Joel Embiid": [
        "Dominant scoring center",
        "NBA MVP",
        "Elite footwork and post game"
    ],

    "Damian Lillard": [
        "Known as Dame Time",
        "Deep shooting range",
        "Known for clutch shots"
    ],

    "Kawhi Leonard": [
        "Elite defender",
        "Two-time NBA champion",
        "Known for clutch playoff performances"
    ],

    "Devin Booker": [
        "Elite shooting guard",
        "Smooth scoring ability",
        "Known for offensive explosions"
    ],

    "Donovan Mitchell": [
        "Explosive scoring guard",
        "Known for huge playoff games",
        "High-flying athlete"
    ],

    "Bam Adebayo": [
        "Versatile defensive big man",
        "Excellent interior defender",
        "Strong all-around center"
    ],

    "Ja Morant": [
        "Extremely athletic guard",
        "Known for explosive dunks",
        "One of the league’s fastest players"
    ],

    "Tyrese Haliburton": [
        "Elite passer",
        "Creative playmaker",
        "Young NBA star guard"
    ],

    "Victor Wembanyama": [
        "Generational young talent",
        "Extremely tall and skilled",
        "Unique shot-blocking ability"
    ],

    "Trae Young": [
        "Elite passer and shooter",
        "Known for deep three-pointers",
        "Dangerous offensive guard"
    ],

    "Jimmy Butler": [
        "Known for playoff performances",
        "Tough two-way player",
        "Nicknamed Jimmy Buckets"
    ]
}

score = 0

# MAIN WINDOW
root = tk.Tk()
root.title("NBA WHO AM I")
root.geometry("700x550")
root.configure(bg="#0B0F1A")

# TITLE
title = tk.Label(
    root,
    text="🏀 NBA WHO AM I 🏀",
    font=("Helvetica", 28, "bold"),
    fg="#F5C518",
    bg="#0B0F1A"
)
title.pack(pady=20)

# SCORE LABEL
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="#0B0F1A"
)
score_label.pack()

# CLUE LABEL
clue_label = tk.Label(
    root,
    text="Press NEXT CLUE to begin!",
    font=("Helvetica", 18),
    fg="white",
    bg="#1C2333",
    wraplength=500,
    width=40,
    height=4
)
clue_label.pack(pady=30)

# INPUT BOX
guess_entry = tk.Entry(
    root,
    font=("Helvetica", 18),
    justify="center",
    width=25,
    bg="#F4F4F4"
)
guess_entry.pack(pady=10)

# RESULT LABEL
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 18, "bold"),
    bg="#0B0F1A"
)
result_label.pack(pady=15)

# GAME VARIABLES
player = ""
clues = []
clue_index = 0

def start_new_round():
    global player, clues, clue_index

    player = random.choice(list(players.keys()))
    clues = players[player]
    clue_index = 0

    clue_label.config(text="Press NEXT CLUE to begin!")
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

def next_clue():
    global clue_index

    if clue_index < len(clues):
        clue_label.config(text=f"💡 {clues[clue_index]}")
        clue_index += 1
    else:
        clue_label.config(text=f"🏀 The Answer Was: {player}")

def check_guess():
    global score

    guess = guess_entry.get()

    if guess.lower() == player.lower():
        score += 1
        score_label.config(text=f"Score: {score}")

        result_label.config(
            text="✅ CORRECT!",
            fg="#00FF99"
        )
    else:
        result_label.config(
            text="❌ Try Again!",
            fg="#FF4C4C"
        )

# BUTTON FRAME
button_frame = tk.Frame(root, bg="#0B0F1A")
button_frame.pack(pady=20)

# NEXT CLUE BUTTON
next_button = tk.Button(
    button_frame,
    text="NEXT CLUE",
    command=next_clue,
    font=("Helvetica", 14, "bold"),
    bg="#1E3A8A",
    fg="white",
    activebackground="#172554",
    activeforeground="white",
    width=15,
    height=2,
    bd=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2"
)
next_button.grid(row=0, column=0, padx=15)

# SUBMIT BUTTON
submit_button = tk.Button(
    button_frame,
    text="SUBMIT GUESS",
    command=check_guess,
    font=("Helvetica", 14, "bold"),
    bg="#065F46",
    fg="white",
    activebackground="#064E3B",
    activeforeground="white",
    width=15,
    height=2,
    bd=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2"
)
submit_button.grid(row=0, column=1, padx=15)

# NEW PLAYER BUTTON
new_round_button = tk.Button(
    root,
    text="NEW PLAYER",
    command=start_new_round,
    font=("Helvetica", 14, "bold"),
    bg="#92400E",
    fg="white",
    activebackground="#78350F",
    activeforeground="white",
    width=18,
    height=2,
    bd=0,
    highlightthickness=0,
    relief="flat",
    cursor="hand2"
)
new_round_button.pack(pady=20)

# START GAME
start_new_round()

root.mainloop()