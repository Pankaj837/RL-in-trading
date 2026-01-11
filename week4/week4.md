# Week 4 — Reinforcement Learning for Trading (Final Project)

## **Overview**
Week 4 focuses on applying Reinforcement Learning to a real-world problem: **algorithmic stock trading**. A complete RL pipeline is built, starting from market data collection to training and evaluating a Q-learning–based trading agent.

This week serves as the **final assignment and project milestone**.

---

## **Key Components**

### **1. Market Data Acquisition**
- Historical stock price data downloaded using **yfinance**
- Closing prices extracted and preprocessed for RL compatibility

---

### **2. Custom Trading Environment**
- Designed a custom environment mimicking a trading setup
- State includes:
  - Current stock price
  - Stock holding status (0 or 1)
- Actions:
  - **Hold**
  - **Buy**
  - **Sell**
- Reward defined as change in portfolio value

---

### **3. Q-Learning Agent**
- Tabular Q-learning implementation
- Parameters:
  - Learning rate (α)
  - Discount factor (γ)
  - Exploration rate (ε)
- ε-greedy policy used during training

---

### **4. Training Process**
- Agent trained over multiple episodes
- Q-values updated using the Bellman equation
- Exploration gradually guides the agent toward profitable actions

---

### **5. Evaluation**
- Trained agent evaluated **without exploration**
- Final portfolio value computed
- Performance compared against a baseline strategy

---

### **6. Buy-and-Hold Baseline**
- Buy one stock on the first day
- Hold until the last day
- Used as a benchmark to assess RL agent performance

---

## **Outcome**
- Demonstrated how RL can be applied to financial decision-making
- Showed limitations of tabular Q-learning in noisy markets
- Established a strong foundation for extensions like:
  - Deep Reinforcement Learning
  - Technical indicators
  - Risk-aware reward functions

---

## **Status**
This repository contains content **up to Week 4 (final project)**.  
