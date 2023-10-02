import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox)

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, 300, 300)
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = 'X'
        self.initBoard()

    def initBoard(self):
        for row in range(3):
            for col in range(3):
                button = QPushButton('', self)
                button.setGeometry(col * 100, row * 100, 100, 100)
                button.setStyleSheet('font-size: 36px;')
                button.clicked.connect(lambda state, row=row, col=col: self.makeMove(row, col))
                self.buttons[row][col] = button

    def makeMove(self, row, col):
        button = self.buttons[row][col]
        if button.text() == '':
            button.setText(self.current_player)
            button.setStyleSheet('font-size: 36px; color: red;' if self.current_player == 'X' else 'font-size: 36px; color: yellow;')
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.checkWin():
                QMessageBox.information(self, 'Tic Tac Toe', f'Player {self.current_player} wins!')
                self.resetBoard()
            elif all(button.text() for row in self.buttons for button in row):
                QMessageBox.information(self, 'Tic Tac Toe', 'It\'s a draw!')
                self.resetBoard()

    def checkWin(self):
        for row in range(3):
            if self.buttons[row][0].text() == self.buttons[row][1].text() == self.buttons[row][2].text() != '':
                return True
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() != '':
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '':
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != '':
            return True
        return False

    def resetBoard(self):
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setStyleSheet('font-size: 36px;')
        self.current_player = 'X'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
