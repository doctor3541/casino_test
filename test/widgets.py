import tkinter as tk

class SlotGrid(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.labels = []

        for r in range(5):
            row = []
            for c in range(5):
                lbl = tk.Label(self, text="❔", font=("Segoe UI Emoji", 36))
                lbl.grid(row=r, column=c, padx=5, pady=5)
                row.append(lbl)
            self.labels.append(row)

    def update(self, grid):
        for r in range(5):
            for c in range(5):
                self.labels[r][c].config(text=grid[r][c], fg="gold")

    def highlight(self, positions):
        for r, c in positions:
            self.labels[r][c].config(fg="green")
