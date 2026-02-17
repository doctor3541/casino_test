import random
from config.symbols import SYMBOLS, WEIGHTS
from config.payouts import PAYOUTS
from engine.paylines import PAYLINES

class GameEngine:
    def __init__(self):
        self.money = 20.0
        self.jackpot = 0.0
        self.free_spins = 0
        self.mode = "FUN"
        self.stats = {
            "spins": 0,
            "wins": 0,
            "total_bet": 0.0,
            "total_win": 0.0
        }

    def can_spin(self, bet):
        return self.free_spins > 0 or self.money >= bet

    def apply_bet(self, bet):
        self.stats["spins"] += 1
        self.stats["total_bet"] += bet

        if self.free_spins:
            self.free_spins -= 1
        else:
            self.money -= bet
            self.jackpot += bet * 0.5

    def generate_grid(self):
        weights = WEIGHTS[self.mode]
        return [
            random.choices(SYMBOLS, weights, k=5)
            for _ in range(5)
        ]

    def evaluate(self, grid, bet):
        best_win = 0
        best_positions = []

        for line in PAYLINES:
            win, pos = self._evaluate_line(grid, line, bet)
            if win > best_win:
                best_win = win
                best_positions = pos

        self.money += best_win
        self.stats["total_win"] += best_win
        if best_win:
            self.stats["wins"] += 1

        return best_win, best_positions

    def _evaluate_line(self, grid, line, bet):
        symbols = [grid[r][c] for r, c in line]
        first = symbols[0]

        if first not in PAYOUTS:
            return 0, []

        count = 1
        for s in symbols[1:]:
            if s == first:
                count += 1
            else:
                break

        if count < 3:
            return 0, []

        payout = PAYOUTS[first][count]
        if payout == "JACKPOT":
            win = self.jackpot
            self.jackpot = 0
        else:
            win = payout * bet

        return win, line[:count]
