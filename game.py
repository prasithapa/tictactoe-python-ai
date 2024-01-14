"""
Prasi Thapa

"""

import pygame
import random
import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

# Constants
WIDTH = 600
HEIGHT = 600
BG_COLOR = (28, 170, 156)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def draw_board(board):
    screen.fill(BG_COLOR)
    for row in range(3):
        for col in range(3):
            square = pygame.Rect(col * (WIDTH // 3), row * (HEIGHT // 3), WIDTH // 3, HEIGHT // 3)
            pygame.draw.rect(screen, (255, 255, 255), square, 3)
            if board[row * 3 + col] == 'X':
                pygame.draw.line(screen, (255, 255, 255), square.topleft, square.bottomright, 3)
                pygame.draw.line(screen, (255, 255, 255), square.bottomleft, square.topright, 3)
            elif board[row * 3 + col] == 'O':
                pygame.draw.circle(screen, (255, 255, 255), square.center, WIDTH // 6, 3)

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    pygame.init()
    clock = pygame.time.Clock()

    while game.empty_squares():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_board(game.board)
        pygame.display.update()

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            draw_board(game.board)
            pygame.display.update()

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game

            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(0.8)
        clock.tick(30)  # Limit the frame rate to 30 FPS

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    players = [HumanPlayer('X'), SmartComputerPlayer('O')]  # List of players
    random.shuffle(players)  # Shuffle the list to randomize the order
    x_player, o_player = players  # Assign the first and second players
    t = TicTacToe()
    play(t, x_player, o_player)
    pygame.quit()
    quit()