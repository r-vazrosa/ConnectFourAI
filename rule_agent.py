import pettingzoo
import numpy as np
from pettingzoo.classic import connect_four_v3

env = connect_four_v3.env(render_mode = 'human')
env.reset()
env.render() # Initial Render

outcome = 0 # The reward given to player 0 (the human)

def get_landing_row(board, col):
    for row in range(5, -1, -1):
        if board[row, col] == 0:
            return row
    return None

def on_board(row, col):
    return ((0 <= row <= 5) and (0 <= col <= 6))

def has_four(board, row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1
        step = 1
        
        while (on_board(row + (dr * step), col + (dc * step))
                and board[row + (dr * step), col + (dc * step)] == 1):
            count += 1
            step += 1
        step = 1
        while (on_board(row + (-dr * step), col + (-dc * step))
                and board[row + (-dr * step), col + (-dc * step)] == 1):
            count += 1
            step += 1
        
        if count >= 4:
            return True
    return False
        
for agent in env.agent_iter(): # Cycle turns of the game
    obs, reward, terminated, truncated, info = env.last()
    player1_board = obs['observation'][:, :, 0]
    player2_board = obs['observation'][:, :, 1]
    game_board = player1_board + player2_board
    legal_moves = []

    for i, move in enumerate(obs['action_mask']):
        if move == 1:
            legal_moves.append(i)

    # If game ends
    if terminated or truncated: 
        action = None
        if agent == 'player_0':
            outcome = reward
    # Game continues
    else: 
        # Player 0 input, catching any errors or illegal moves
        if agent == "player_0":

            valid = False
            while not valid:
                try:
                    move = int(input("Player 0 Move (0-6): "))
                    if move in legal_moves:
                        action = move
                        valid = True
                    else:
                        print("Column full or invalid, try again.")
                except ValueError:
                    print("Enter a number between 0-6")
        # Rule based agent
        else:
            winning_move = None
            blocking_move = None

            for move in legal_moves:
                row = get_landing_row(game_board, move)
                if row != None:
                    board_copy = player1_board.copy()
                    board_copy[row, move] = 1
                    if has_four(board_copy, row, move):
                        winning_move = move
                        break
            
            if winning_move == None:
                for move in legal_moves:
                    row = get_landing_row(game_board, move)
                    if row != None:
                        board_copy = player2_board.copy()
                        board_copy[row, move] = 1
                        if has_four(board_copy, row, move):
                            blocking_move = move
                            break
   
            if winning_move != None:
                action = winning_move
                print('I found a winning move!')
            elif blocking_move != None:
                action = blocking_move
                print('I blocked a win!')

            elif 3 in legal_moves:
                action = 3
            else:
                action = np.random.choice(legal_moves)

    
    
    env.step(action)

    env.render()

# Message based on Player 0's reward
if outcome == -1:
    print("You Lose!")
if outcome == 0:
    print("It's a Draw")
if outcome == 1:
    print('You Win!')