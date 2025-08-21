import pettingzoo
from pettingzoo.classic import connect_four_v3

env = connect_four_v3.env()
env.reset()

print('Agents', env.agents)
