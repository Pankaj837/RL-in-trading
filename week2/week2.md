# Week 2 — Introduction to Reinforcement Learning and Bandits

## **Overview**  
Week 2 introduced the fundamentals of **Reinforcement Learning (RL)** through simple yet important decision-making problems. The primary focus was on understanding how an agent interacts with an environment and learns from rewards, using the **Multi-Armed Bandit** problem as a starting point.

---

## **Topics Covered**  

### **Introduction to Reinforcement Learning**  
- Basic RL framework: agent, action, reward, environment  
- Difference between supervised learning and reinforcement learning  
- Role of reward signals in guiding learning  

The introductory lectures helped build intuition before moving to formal algorithms.

---

### **Multi-Armed Bandit Problem**  
- Understanding the bandit setup as a repeated decision-making problem  
- Exploration vs exploitation trade-off  
- Importance of balancing short-term reward and long-term performance  

The bandit problem was studied using examples from **Sutton and Barto (Chapters 1 & 2)**.

---

### **Greedy Algorithm**  
- Always selects the action with the highest estimated reward  
- Simple to implement but lacks exploration  
- Can converge to suboptimal actions due to insufficient exploration  

---

### **Epsilon-Greedy Algorithm**  
- Introduces exploration by choosing a random action with probability **ε**  
- Exploitation is performed with probability **(1 − ε)**  
- Helps avoid getting stuck with suboptimal actions  

---

## **Algorithms Implemented**  
- **Greedy** action selection  
- **Epsilon-greedy** action selection  
- Reward estimation using incremental averaging  

Both algorithms were implemented and tested on the same bandit environment.

---

## **Experiments & Observations**  
- **Greedy policy** performs well initially but can fail if early estimates are misleading  
- **Epsilon-greedy policy** achieves better long-term performance due to exploration  
- Even small exploration (**small ε**) significantly improves average reward  

---

## **Conclusion & Next Steps**  
Week 2 provided a solid introduction to reinforcement learning concepts using the multi-armed bandit problem. Implementing and comparing greedy and epsilon-greedy algorithms helped build intuition about exploration strategies.

In **Week 3**, the focus will shift to **Markov Decision Processes (MDPs)** and the mathematical formulation of reinforcement learning problems.

