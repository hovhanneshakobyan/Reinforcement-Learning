♠️ Blackjack with Monte Carlo Methods
A hands-on project inspired by Sutton & Barto’s "Reinforcement Learning: An Introduction" (2nd Edition, Chapter 5)

📘 Overview
This project explores how an AI agent can learn to play Blackjack using Monte Carlo methods, a set of powerful techniques in Reinforcement Learning (RL) that learn from experience without needing a model of the environment.

Whether you're a beginner in AI or a seasoned developer curious about Monte Carlo methods, this project walks through building a smart Blackjack-playing agent from scratch using three classic RL approaches.

🎯 Project Goals
Simulate a simplified Blackjack environment (infinite-deck, episodic).

Apply three Monte Carlo techniques to learn an optimal strategy.

Understand the theory behind model-free learning and see it in action.

🧠 What You'll Learn
✅ How Monte Carlo methods work in reinforcement learning
✅ Differences between on-policy and off-policy learning
✅ How agents learn from episodes without knowing environment dynamics
✅ How to apply importance sampling to evaluate policies

.

Techniques Used

1. Monte Carlo Exploring Starts (MC-ES)
Learns an optimal policy by exploring all state-action pairs.

Requires the first action of each episode to be randomly chosen (to ensure all actions are tried).

2. On-Policy MC Control with ε-Greedy Policy
The agent learns while following a slightly random (ε-greedy) version of its current policy.

Balances exploration (trying new actions) with exploitation (using the best-known action).

3. Off-Policy MC Prediction via Importance Sampling
Evaluates one policy (target) while following a different one (behavior).

Uses importance sampling to correct for the difference between policies.



📚 Reference
This project is based on the example from:

Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.)
Specifically, see Chapter 5 – Monte Carlo Methods.