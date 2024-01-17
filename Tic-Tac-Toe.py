import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.buttons=[]
        for i in range(3):
            row_button=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=20,height=10,command=lambda i=i,j=j:self.move_method(i,j))
                button.grid(row=i,column=j)
                row_button.append(button)
            self.buttons.append(row_button)
    def move_method(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.is_winner(self.current_player):
                messagebox.showinfo("Game Winner "+self.current_player)
                self.window.quit() 
            elif self.is_draw():
                messagebox.showinfo("Its Tie ")
                self.window.quit() 
            self.current_player="O" if self.current_player=="X" else "X"
    def is_winner(self,player):
        for i in range(3):
            if player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
                self.buttons[i][0].config(bg="lightgreen")
                self.buttons[i][1].config(bg="lightgreen")
                self.buttons[i][2].config(bg="lightgreen")
                return True
            if player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                self.buttons[0][i].config(bg="lightgreen")
                self.buttons[1][i].config(bg="lightgreen")
                self.buttons[2][i].config(bg="lightgreen")
                return True
        if player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
                self.buttons[0][0].config(bg="lightgreen")
                self.buttons[1][1].config(bg="lightgreen")
                self.buttons[2][2].config(bg="lightgreen")
                return True
        if player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
                self.buttons[0][2].config(bg="lightgreen")
                self.buttons[1][1].config(bg="lightgreen")
                self.buttons[2][0].config(bg="lightgreen")
                return True
        return False
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
              
        

    def run(self):
        self.window.mainloop()
game=TicTacToe()
game.run()
