import pettingzoo
import numpy as np
from pettingzoo.classic import connect_four_v3

env = connect_four_v3.env(render_mode = 'human')
env.reset()
env.render() # Initial Render

outcome = 0 # The reward given to player 0 (the human)

for agent in env.agent_iter(): # Cycle turns of the game
    obs, reward, terminated, truncated, info = env.last()

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
            print("obs['observation'] shape:", getattr(obs.get("observation", None), "shape", None))

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
            if 3 in legal_moves:
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