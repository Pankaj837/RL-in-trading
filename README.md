# RL-in-trading

This repository documents my week-by-week progress on the WiDS: Reinforcement Learning in Trading project. It contains concise weekly reports and solved problems for Weeks 1–4, along with key results and next steps, culminating in a final applied RL project in trading.

## Project goal

Build a solid practical understanding of reinforcement learning and related tools, then apply those ideas to simple decision-making tasks with a view toward trading-related problems.

## Repo layout

```
RL-in-Trading-WiDS
├── README.md                
├── requirements.txt        
├── Week1
│   ├── Week1.md             
│   └── solutions          
├── Week2
│   ├── Week2.md
│   └── solutions
├── Week3
│   ├── Week3.md
│   └── solutions
├── Week4
    ├── Week4.md
    └── solutions
```

Each `WeekX.md` will contain:

* short overview of the week
* topics covered and why they matter
* problems/assignments solved 
* key results and figures 

The `solutions/` folder holds compact code files or short notes that implement the solved problems for that week.

## What to expect 

**Week 1 — Foundations**

* Python essentials for data work (types, control flow, functions)
* NumPy basics: arrays, broadcasting, vectorized ops
* Pandas basics: loading and inspecting tabular data
* Matplotlib basics: simple plots and saving figures
* Short exercises for algorithmic thinking and debugging

**Week 2 — Reinforcement Learning (Bandits)**

* Reinforcement learning intro and exploration vs exploitation
* Multi-armed bandit problem (Sutton & Barto — Ch.1–2)
* Implementations: greedy and ε-greedy policies
* Experimental comparison and interpretation of rewards

**Week 3 — MDPs & Practical RL**

* Markov Decision Processes: states, actions, rewards, transitions
* Value-based methods and basic planning algorithms (value iteration / policy iteration)
* Practical notes on extracting and interpreting financial time-series (close, adj close, rolling mean, dividends)
* Assignment-based exercises from Grokking / course materials

**Week 4 — Reinforcement Learning Trading Agent (Final Project)**

- Built a **custom trading environment** using historical stock price data
- Implemented a **tabular Q-learning agent** with Buy / Sell / Hold actions
- Trained the agent using ε-greedy exploration
- Evaluated performance on unseen data
- Benchmarked against a **Buy-and-Hold baseline**
- Analyzed strengths and limitations of tabular RL in financial markets

## Dependencies (summary)

Common libraries used across weeks (listed here for convenience):

* `numpy`, `pandas`, `matplotlib`
* `jupyter` (for interactive exploration)
* `yfinance`
* `torch` / `gym` for advanced RL experiments


## How to review the work

1. Open `WeekX/WeekX.md` to read the weekly summary and findings.
2. Check `WeekX/solutions/` for minimal runnable code or short scripts that implement the solved problems.

## Status & next steps

* This repository contains the completed work for Weeks 1, 2, 3 and 4 of the WiDS project.
* The repository is submitted as a Final report 

