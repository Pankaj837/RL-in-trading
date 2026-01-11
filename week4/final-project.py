# 1. Install and Import Libraries

!pip install yfinance numpy pandas matplotlib
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# 2. Download Market Data

symbol = "AAPL"

data = yf.download(symbol, start="2018-01-01", end="2023-01-01")

prices = data["Close"].values.flatten()

print("Trading days:", len(prices))
print("Sample price:", prices[0], type(prices[0]))


# 3. Trading Environment

class TradingEnv:
    def __init__(self, prices):
        self.prices = prices
        self.reset()

    def reset(self):
        self.t = 0
        self.cash = 10000
        self.stock = 0
        self.done = False
        return self._get_state()

    def _get_state(self):
        return np.array([self.prices[self.t], self.stock])

    def step(self, action):
        price = self.prices[self.t]

        # 0: Hold
        if action == 1 and self.cash >= price:        # Buy
            self.cash -= price
            self.stock = 1

        elif action == 2 and self.stock == 1:          # Sell
            self.cash += price
            self.stock = 0

        # move forward
        self.t += 1
        if self.t >= len(self.prices) - 1:
            self.done = True

        # portfolio value
        reward = self.cash + self.stock * self.prices[self.t]

        return self._get_state(), reward, self.done


# 4. Q-Learning Setup

# Q-table: states = time steps, actions = [Hold, Buy, Sell]
Q = np.zeros((len(prices), 3))

# hyperparameters
alpha = 0.1      # learning rate
gamma = 0.95     # discount factor
epsilon = 0.1    # exploration rate


# 5. Train the Agent

env = TradingEnv(prices)
episodes = 200

for episode in range(episodes):
    state = env.reset()

    while not env.done:
        t = env.t

        # epsilon-greedy
        if np.random.rand() < epsilon:
            action = np.random.choice(3)
        else:
            action = np.argmax(Q[t])

        _, reward, done = env.step(action)

        # next state index
        t_next = min(env.t, len(prices) - 1)

        # Q-learning update
        Q[t, action] += alpha * (
            reward + gamma * np.max(Q[t_next]) - Q[t, action]
        )

print("Training completed")


# 6. Evaluate Trained Agent

env = TradingEnv(prices)
state = env.reset()

while not env.done:
    t = env.t
    action = np.argmax(Q[t])   # no exploration
    state, reward, done = env.step(action)

final_value = reward
print("RL Agent final portfolio value:", final_value)


# 7. Buy and Hold Baseline

initial_cash = 10000
first_price = prices[0]
last_price = prices[-1]

buy_and_hold_value = initial_cash - first_price + last_price
print("Buy-and-Hold final portfolio value:", buy_and_hold_value)





