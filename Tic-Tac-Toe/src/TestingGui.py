import tkinter as tk
from tkinter import messagebox
from state import State ,get_all_states
from player import RLPlayer, HumanPlayer
from judge import Judge


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.buttons = {}
        self.board = None
        self.current_player = None
        self.game_running = False
        self.all_states = get_all_states(3, 3)

        self.create_game_board()

    def create_game_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=" ", font="Arial 20", width=5, height=2,
                                   command=lambda r=row, c=col: self.on_cell_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

        self.reset_game_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_game_button.grid(row=3, column=0, columnspan=3)

    def reset_game(self):
        for button in self.buttons.values():
            button.config(text=" ", state="normal")

        self.board = State()
        self.game_running = True

        self.current_player = HumanPlayer()  # Assume human goes first
        self.current_player.set_symbol(1)

        self.rl_player = RLPlayer(self.all_states, epsilon=0)
        self.rl_player.set_symbol(-1)

        self.judge = Judge(self.current_player, self.rl_player)
        self.current_player.set_state(self.board)
        self.rl_player.set_state(self.board)

    def on_cell_click(self, row, col):
        if not self.game_running:
            return

        # Check if the cell is already taken
        if self.board.data[row][col] != 0:
            return

        # Human makes the move
        self.board.data[row][col] = self.current_player.symbol
        self.current_player.set_state(self.board)
        self.update_board()

        if self.check_game_over():
            return

        # Switch to RL player
        self.rl_player_action()

    def rl_player_action(self):
        # RL player makes the move
        i, j, symbol = self.rl_player.act()
        self.board.data[i][j] = symbol
        self.rl_player.set_state(self.board)
        self.update_board()

        self.check_game_over()

    def update_board(self):
        # Update buttons to reflect the current state
        for i in range(3):
            for j in range(3):
                symbol = self.board.data[i][j]
                if symbol == 1:
                    self.buttons[(i, j)].config(text="X", state="disabled")
                elif symbol == -1:
                    self.buttons[(i, j)].config(text="O", state="disabled")

    def check_game_over(self):
        if self.board.is_game_ended():
            winner = self.board.winner
            if winner == 1:
                self.display_winner("Human wins!")
            elif winner == -1:
                self.display_winner("RL Agent wins!")
            else:
                self.display_winner("It's a tie!")
            return True
        return False

    def display_winner(self, message):
        self.game_running = False
        messagebox.showinfo("Game Over", message)
        self.reset_game()


def main():
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    gui.reset_game()  # Initialize the game board
    root.mainloop()


if __name__ == "__main__":
    main()
