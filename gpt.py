import tkinter as tk
from tkinter import font as tkfont

class FancyCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy Counter")
        
        # Fonts
        self.counter_font = tkfont.Font(family='Helvetica', size=36, weight=tkfont.BOLD)
        self.button_font = tkfont.Font(family='Helvetica', size=16)
        
        # Counter value
        self.counter = tk.IntVar(value=0)
        
        # Counter label
        self.label = tk.Label(root, textvariable=self.counter, font=self.counter_font, fg="red")
        self.label.pack(pady=50)
        
        # Increment button
        self.inc_button = tk.Button(root, text="Increment", font=self.button_font, command=self.increment)
        self.inc_button.pack(side="left", padx=50)
        
        # Decrement button
        self.dec_button = tk.Button(root, text="Decrement", font=self.button_font, command=self.decrement)
        self.dec_button.pack(side="right", padx=50)
        
        # Update label color
        self.update_label_color()
        
    def increment(self):
        current_value = self.counter.get()
        self.counter.set(current_value + 1)
        self.update_label_color()
        
    def decrement(self):
        current_value = self.counter.get()
        self.counter.set(current_value - 1)
        self.update_label_color()
        
    def update_label_color(self):
        current_value = self.counter.get()
        if current_value > 0:
            self.label.config(fg="green")
        elif current_value == 0:
            self.label.config(fg="red")
        else:
            self.label.config(fg="black")


    def save_current_value(self):
        """Save the current counter value."""
        self.save_point = self.counter.get()

    def load_saved_value(self):
        """Load the saved counter value."""
        self.counter.set(self.save_point)
        self.update_label_color()

if __name__ == "__main__":
    root = tk.Tk()
    counter_app = FancyCounter(root)
    root.mainloop()