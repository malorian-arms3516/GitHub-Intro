import tkinter as tk
from tkinter import ttk


class HelloApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Greeting App")
        self.root.geometry("360x220")
        self.root.resizable(False, False)

        frame = ttk.Frame(root, padding=20)
        frame.pack(expand=True, fill="both")

        prompt_label = ttk.Label(frame, text="What's your name?", font=("Segoe UI", 11))
        prompt_label.pack(pady=(0, 10))

        self.name_entry = ttk.Entry(frame, font=("Segoe UI", 11), width=25)
        self.name_entry.pack(pady=(0, 12))
        self.name_entry.focus()

        greet_button = ttk.Button(frame, text="Say Hello", command=self.say_hello)
        greet_button.pack(pady=(0, 15))

        self.greeting_label = ttk.Label(frame, text="Hello, World!", font=("Segoe UI", 12, "bold"))
        self.greeting_label.pack()

        self.root.bind("<Return>", lambda event: self.say_hello())

    def say_hello(self):
        name = self.name_entry.get().strip()
        if name:
            self.greeting_label.config(text=f"Hello, {name}!")
        else:
            self.greeting_label.config(text="Hello, World!")


def main():
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()