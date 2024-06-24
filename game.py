import tkinter as tk
from tkinter import messagebox
import random

# Define the game logic
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}")

    # Update the score
    if result == "You win!":
        scores["user"] += 1
    elif result == "Computer wins!":
        scores["computer"] += 1
    score_label.config(text=f"Score - You: {scores['user']} Computer: {scores['computer']}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def reset_game():
    scores["user"] = 0
    scores["computer"] = 0
    score_label.config(text="Score - You: 0 Computer: 0")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Main frame
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Instruction label
instruction_label = tk.Label(main_frame, text="Choose Rock, Paper, or Scissors:")
instruction_label.grid(row=0, column=0, columnspan=3)

# Buttons for user choices
rock_button = tk.Button(main_frame, text="Rock", command=lambda: play("Rock"))
rock_button.grid(row=1, column=0)

paper_button = tk.Button(main_frame, text="Paper", command=lambda: play("Paper"))
paper_button.grid(row=1, column=1)

scissors_button = tk.Button(main_frame, text="Scissors", command=lambda: play("Scissors"))
scissors_button.grid(row=1, column=2)

# Result label
result_label = tk.Label(main_frame, text="", font=("Arial", 12), pady=10)
result_label.grid(row=2, column=0, columnspan=3)

# Score tracking
scores = {"user": 0, "computer": 0}
score_label = tk.Label(main_frame, text="Score - You: 0 Computer: 0", font=("Arial", 12), pady=10)
score_label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(main_frame, text="Reset Scores", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)

# Run the application
root.mainloop()
