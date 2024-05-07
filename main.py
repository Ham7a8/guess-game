import random
import tkinter as tk
from tkinter import ttk

class HigherLowerGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Higher Lower Guessing Game")
        self.geometry("350x220")
        self.configure(bg="#f0f0f0")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label_info = ttk.Label(self, text="Guess a number between 1 and 100:", font=("Arial", 12), background="#f0f0f0")
        self.label_info.pack(pady=10)
        
        self.entry = ttk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())
        
        self.label_result = ttk.Label(self, text="", font=("Arial", 12), background="#f0f0f0")
        self.label_result.pack(pady=5)
        
        self.label_attempts = ttk.Label(self, text="", font=("Arial", 12), background="#f0f0f0")
        self.label_attempts.pack(pady=5)
        
        self.button = ttk.Button(self, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)
        
        self.update_attempts_label()
    
    def check_guess(self):
        guess = self.entry.get()
        
        if not guess.isdigit():
            self.label_result.config(text="Please enter a valid number.", foreground="red")
            return
        
        guess = int(guess)
        self.attempts += 1
        
        if guess == self.secret_number:
            self.label_result.config(text=f"You guessed the number in {self.attempts} attempts.", foreground="green")
            self.restart_game()
        elif guess < self.secret_number:
            self.label_result.config(text="Higher!", foreground="blue")
        else:
            self.label_result.config(text="Lower!", foreground="blue")
        
        self.update_attempts_label()
    
    def update_attempts_label(self):
        self.label_attempts.config(text=f"Attempts: {self.attempts}")
    
    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.update_attempts_label()

if __name__ == "__main__":
    game = HigherLowerGame()
    game.mainloop()
