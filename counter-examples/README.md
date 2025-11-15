# Access-Control Queue – Differential Semi-Gradient SARSA

This project implements the classic **Access-Control Queuing Task** from Sutton & Barto’s *Reinforcement Learning* (Chapter 10). The goal is to learn an optimal policy for accepting or rejecting incoming customers with different priorities when a limited number of servers are available. The solution uses **differential semi-gradient SARSA** together with **tile coding** for function approximation.

---

## 📌 Problem Overview

- There are **10 servers**, each may be free or busy.
- Customers arrive with **4 priority levels** (0–3).
- Rewards for accepting customers are **1, 2, 4, 8** depending on priority.
- Busy servers become free each timestep with probability **0.06**.
- If no servers are free, the agent must reject the customer.
- The objective is to **maximize long-term average reward** (continuing task, no discounting).

At every timestep, the agent observes:
- Current **number of free servers**
- Current **customer priority**

and chooses either:
- `accept`  
- `reject`

---

## ⚙️ Method

### ✅ Differential Semi-Gradient SARSA
Used for continuing tasks to learn:
- The **average reward**  
- The **action-value function** \( q(s, a) \)

### ✅ Tile Coding (Function Approximation)
Tile coding converts `(free_servers, priority, action)` into sparse feature vectors across multiple tilings.  
This provides:
- Generalization across states  
- Stable learning using linear function approximation  
- A scalable alternative to tabular methods  

The implementation includes Sutton’s official `IHT` and `tiles` utilities.

---

## 🚀 Training

Training runs for **1,000,000 steps** using:
- ε-greedy exploration  
- Semi-gradient SARSA updates  
- Weight updates per active tile  
- Average-reward updates using step-size β  

During training, we also track how frequently each number of free servers occurs.

---

## 📊 Output

After learning, the script produces:

- **Value curves** for each priority  
- **Policy heatmap** (0 = Reject, 1 = Accept)  
- **Frequency distribution** of free servers  
- Saved plot: `figure_10_5.png`  

These results reproduce the behavior shown in Figure 10.5 from the RL textbook.

---


