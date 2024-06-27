import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(input, master):
        input.master = master
        input.master.title("Tic Tac Toe")
        input.player = 'X'
        input.board = ['' for _ in range(9)]
        input.buttons = []
        input.create_widgets()

    def create_widgets(input):
        for i in range(9):
            button = tk.Button(input.master, text='', font=('normal', 20), width=5, height=2,
                               command=lambda i=i: input.click(i))
            button.grid(row=i // 3, column=i % 3)
            input.buttons.append(button)
        input.reset_button = tk.Button(input.master, text='Reset', command=input.reset)
        input.reset_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def click(input, index):
        if input.board[index] == '' and input.check_winner() is False:
            input.board[index] = input.player
            input.buttons[index].config(text=input.player)
            if input.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {input.player} wins!")
            elif '' not in input.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            input.player = 'O' if input.player == 'X' else 'X'

    def check_winner(input):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)             
        ]
        for combo in win_combinations:
            if input.board[combo[0]] == input.board[combo[1]] == input.board[combo[2]] != '':
                return True
        return False

    def reset(input):
        input.board = ['' for _ in range(9)]
        for button in input.buttons:
            button.config(text='')
        input.player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
