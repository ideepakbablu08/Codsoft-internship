import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image



user_score = 0
comp_score = 0
round_count = 0

def determine_winner(user_choice, comp_choice):
    global user_score, comp_score

    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        user_score += 1
        return "You win!"
    else:
        comp_score += 1
        return "You lose!"

def user_choice(choice):
    global round_count

    if round_count < 5:
        comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result = determine_winner(choice, comp_choice)
        result_label.config(text=f"Computer chose: {comp_choice}\n{result}")
        round_count += 1

        attempts_label.config(text=f"Attempts: {round_count}/5")

        if round_count == 5:
            declare_winner()

def declare_winner():
    global user_score, comp_score
    if user_score > comp_score:
        final_result = "Congratulations! You won the game!"
    elif user_score < comp_score:
        final_result = "Sorry! The computer won the game!"
    else:
        final_result = "It's a tie game!"

    messagebox.showinfo("Game Over", final_result)
    reset_game()

def reset_game():
    global user_score, comp_score, round_count
    user_score = 0
    comp_score = 0
    round_count = 0
    result_label.config(text="")
    attempts_label.config(text="Attempts: 0/5")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry('1000x750')
root.resizable(0, 0)

path = r"C:\Users\Deepak kumar\Downloads\rock2-game.png"
bg = ImageTk.PhotoImage(Image.open(path))
img1 = tk.Label(root, image=bg)
img1.place(x=0, y=0)

attempts_label = tk.Label(root, text="Attempts: 0/5", font=('Helvetica', 14), bg='black', fg='white')
attempts_label.place(x=10, y=10)

tk.Label(root, text="Rock, Paper, or Scissors", font=('Helvetica', 16), bg='black', fg='white').pack()

rock_button = tk.Button(root, text="ROCK", font=('Helvetica', 14), width=15, bg='black', fg='white', command=lambda: user_choice('Rock'))
rock_button.place(x=100, y=615)

scissors_button = tk.Button(root, text="SCISSORS", font=('Helvetica', 14), width=15, bg='black', fg='white', command=lambda: user_choice('Scissors'))
scissors_button.place(x=400, y=615)

paper_button = tk.Button(root, text="PAPER", font=('Helvetica', 14), bg='black', width=15, fg='white', command=lambda: user_choice('Paper'))
paper_button.place(x=700, y=615)

result_label = tk.Label(root, text="", font=('Helvetica', 16), bg='yellow2', fg='black')
result_label.place(x=400, y=150)





root.mainloop()
