# first run this in colab ( bandit.py ) 
import numpy as np

class Bandit:
    def __init__(self, mean=0, stddev=1):
        self.__mean = mean
        self.__stddev = stddev

    '''This method simulates pulling the lever of the bandit and returns the reward'''
    def pullLever(self):
        return np.random.normal(self.__mean, self.__stddev)



# Greedy algorithm Implementation
def run_greedy(iters=1000):
    Q = [0.0]*len(bandits)
    N = [0]*len(bandits)
    rewards = []

    for _ in range(iters):
        a = Q.index(max(Q))
        r = bandits[a].pullLever()
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
        rewards.append(r)

    return rewards

# ε-greedy algorithm
def run_epsilon_greedy(epsilon, iters=1000):
    Q = [0.0]*len(bandits)
    N = [0]*len(bandits)
    rewards = []

    for _ in range(iters):
        if random.random() < epsilon:
            a = random.randrange(len(bandits))
        else:
            a = Q.index(max(Q))

        r = bandits[a].pullLever()
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
        rewards.append(r)

    return rewards

# Optimistic initial values
  def run_optimistic_greedy(Q1=10, epsilon=0.1, iters=1000):
    Q = [Q1]*len(bandits)
    N = [0]*len(bandits)
    rewards = []

    for _ in range(iters):
        if random.random() < epsilon:
            a = random.randrange(len(bandits))
        else:
            a = Q.index(max(Q))

        r = bandits[a].pullLever()
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
        rewards.append(r)

    return rewards

# UCB ( Upper Confidence Bound )
import math

def run_ucb(c, iters=1000):
    Q = [0.0]*len(bandits)
    N = [0]*len(bandits)
    rewards = []

    for t in range(1, iters+1):
        ucb_vals = []
        for i in range(len(bandits)):
            if N[i] == 0:
                ucb_vals.append(float('inf'))
            else:
                ucb_vals.append(Q[i] + c*math.sqrt(math.log(t)/N[i]))

        a = ucb_vals.index(max(ucb_vals))
        r = bandits[a].pullLever()
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
        rewards.append(r)

    return rewards
