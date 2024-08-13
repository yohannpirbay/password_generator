import tkinter as tk
from tkinter import messagebox
from password_logic import generate_password
from pyperclip import copy

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        tk.Label(self.root, text="Generated Password:").pack(pady=(10,0))

        self.password_frame = tk.Frame(self.root)
        self.password_frame.pack(pady=(10,0))

        self.password_display = tk.Entry(self.password_frame, width=30, justify="center")
        self.password_display.insert(0, "Password")
        self.password_display.config(state="readonly")
        self.password_display.grid(row=0, column=0, padx=(90, 4), pady=5, sticky="w")

        self.copy_button = tk.Button(self.password_frame, text="Copy", command=self.on_copy)
        self.copy_button.grid(row=0, column=1, padx=5)

        self.length_frame = tk.Frame(self.root)
        self.length_frame.pack(pady=(30,0))

        tk.Label(self.length_frame, text="Password Length:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.length_slider = tk.Scale(self.length_frame, from_=8, to=32, orient=tk.HORIZONTAL, width=10)
        self.length_slider.grid(row=0, column=1, padx=5, pady=(0, 17))

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.on_generate_password)
        self.generate_button.pack(pady=(10,0))

        self.root.mainloop()
    
    def on_generate_password(self):
        length = int(self.length_slider.get())
        generated_password = generate_password(length)
        self.password_display.config(state=tk.NORMAL)
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, generated_password)
        self.password_display.config(state="readonly")
    
    def on_copy(self):
        copy(self.password_display.get())

def run():
    MyGUI()

