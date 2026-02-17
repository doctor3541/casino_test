import tkinter as tk
from engine.engine import GameEngine
from gui.widgets import SlotGrid

class SlotApp:
    def __init__(self, root):
        self.root = root
        self.engine = GameEngine()

        root.title("🎰 Casino Elite PRO")
        root.geometry("900x800")

        self.grid = SlotGrid(root)
        self.grid.pack(pady=20)

        self.info = tk.Label(root, text="")
        self.info.pack()

        self.spin_btn = tk.Button(root, text="SPIN", command=self.spin)
        self.spin_btn.pack()

    def spin(self):
        bet = 0.5
        if not self.engine.can_spin(bet):
            return

        self.engine.apply_bet(bet)
        grid = self.engine.generate_grid()
        self.grid.update(grid)

        win, pos = self.engine.evaluate(grid, bet)
        self.info.config(text=f"Výhra: {win:.2f} €")
        self.grid.highlight(pos)
