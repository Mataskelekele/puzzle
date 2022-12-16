import numpy as np
from puzzle import SquarePuzzle
from agent.q_learning import QLearningAgent

if __name__ == "__main__":
    env = SquarePuzzle(edge_length=2)
    agent = QLearningAgent()
    agent.learn(env, episode_count=150000,gamma=0.95)