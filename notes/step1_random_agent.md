#Step 1: Random Agent
- Learned that the environment in this case is the board and rules of the game
- env.last() gives the information of the board as well as state of the game and reward for previous action
- env.action_space(agent) determines what moves are avaliable to the current agent, and .sample() picks a move out of that list
- Moves happen after the game to give rewards to the agents
- Iteration is based on queue, cycling through the same list

All in all, I learned how to interact with pettingzoo and make the game turns occur. I learned what it means to think about when it comes to the environment, and that humans are considered agents if they are playing. This was a good way to get into the future agents I will be working on since it gave be a foundation of understanding.