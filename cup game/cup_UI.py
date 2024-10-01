import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def generate_random_order():
    array = [1, 2, 3, 4, 5]
    random.shuffle(array)
    return array

def get_correct_placements(secret_order, user_guess):
    correct_count = 0
    for i in range(len(secret_order)):
        if secret_order[i] == user_guess[i]:
            correct_count += 1
    return correct_count

class NumberOrderingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Ordering Game")
        self.root.configure(bg="#f0f8ff")

        self.secret_order = generate_random_order()
        self.user_guess = [1, 2, 3, 4, 5]
        self.attempts = 0
        self.first_selected = None
        self.high_score = self.load_high_score()

        self.images = {}
        for i in range(1, 6):
            img = Image.open(f"{i}.png").resize((100, 100))
            self.images[i] = ImageTk.PhotoImage(img)

        self.instruction_label = tk.Label(
            self.root, text="Swap numbers to match the secret order", font=('Helvetica', 16, 'bold'),
            bg="#f0f8ff", fg="#333")
        self.instruction_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        self.buttons = []
        for i in range(5):
            button = tk.Button(self.button_frame, image=self.images[self.user_guess[i]],
                               relief="flat", bd=0, highlightthickness=0, command=lambda i=i: self.select_number(i))
            button.pack(side="left", padx=10)
            self.buttons.append(button)

        self.feedback_label = tk.Label(self.root, text="", font=('Helvetica', 14),
                                       bg="#f0f8ff", fg="#333")
        self.feedback_label.pack(pady=20)

        self.high_score_label = tk.Label(self.root, text=f"High Score: {self.high_score}", font=('Helvetica', 14),
                                          bg="#f0f8ff", fg="#333")
        self.high_score_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        # Label for current attempts
        self.attempt_label = tk.Label(self.root, text=f"Attempts: {self.attempts}", font=('Helvetica', 14),
                                       bg="#f0f8ff", fg="#333")
        self.attempt_label.pack(pady=10)

        # Check Order button
        self.check_button = tk.Button(
            self.root,
            text="Check Order",
            font=('Helvetica', 14),
            bg="#f0f8ff",
            fg="#000000",
            relief="flat",
            bd=0,
            highlightthickness=0,
            highlightbackground="#f0f8ff",
            highlightcolor="#f0f8ff",
            activebackground="#f0f8ff",
            activeforeground="#fff",
            command=self.check_guess,
            state="disabled"
        )
        self.check_button.pack(pady=10)

        self.reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=('Helvetica', 14),
            bg="#f0f8ff",
            fg="#000000",
            relief="flat",
            bd=0,
            highlightthickness=0,
            highlightbackground="#f0f8ff",
            highlightcolor="#f0f8ff",
            activebackground="#f0f8ff",
            activeforeground="#fff",
            command=self.reset_game
        )
        self.reset_button.pack(pady=10)

    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as file:
                try:
                    return int(file.read())
                except ValueError:
                    return float('inf')
        return float('inf')

    def save_high_score(self):
        if self.attempts < self.high_score:
            with open("highscore.txt", "w") as file:
                file.write(str(self.attempts))
            self.high_score = self.attempts
            self.high_score_label.config(text=f"High Score: {self.high_score}")

    def select_number(self, index):
        if self.first_selected is None:
            self.first_selected = index
            self.buttons[index].config(bg="#ffdac1")
        else:
            self.swap_numbers(self.first_selected, index)
            self.first_selected = None
            self.check_button.config(state="normal")

    def swap_numbers(self, first_index, second_index):
        self.user_guess[first_index], self.user_guess[second_index] = (
            self.user_guess[second_index], self.user_guess[first_index])

        for i in range(5):
            self.buttons[i].config(image=self.images[self.user_guess[i]])

        # Remove attempts increment here

    def check_guess(self):
        self.attempts += 1  # Increment attempts here
        correct_placement = get_correct_placements(self.secret_order, self.user_guess)
        self.feedback_label.config(text=f"Correctly placed numbers: {correct_placement}")

        if correct_placement == 5:
            messagebox.showinfo("Congratulations!", f"You've guessed the correct order in {self.attempts} swaps!")
            self.save_high_score()
            self.reset_game()


    def reset_game(self):
        self.secret_order = generate_random_order()
        self.user_guess = [1, 2, 3, 4, 5]
        self.attempts = 0
        self.first_selected = None

        for i in range(5):
            self.buttons[i].config(image=self.images[self.user_guess[i]])

        self.feedback_label.config(text="")
        self.check_button.config(state="disabled")
        self.attempt_label.config(text=f"Attempts: {self.attempts}")  # Reset attempts label

def main():
    root = tk.Tk()
    game = NumberOrderingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()