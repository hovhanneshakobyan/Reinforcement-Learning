🧩 Gridworld – Solving with Dynamic Programming (DP)
Using Dynamic Programming (DP) methods to solve the Gridworld problem, assuming a known model of the environment.

📘 Overview
This project focuses on solving the Gridworld problem using Dynamic Programming (DP) techniques. The environment in this case is fully known, meaning the transition model (how the agent moves between states) and reward function (the reward it receives after each action) are explicitly given.

We will implement two core DP methods:

Policy Iteration: A method that alternates between policy evaluation and policy improvement.

Value Iteration: A method that iteratively improves the value function and the policy simultaneously.

Both methods work by calculating the optimal values and policies based on the agent's knowledge of the environment.

🌍 The Gridworld Environment
The Gridworld is a deterministic environment with:

Grid size: A fixed-size grid (e.g., 4x4).

Actions: The agent can move up, down, left, or right.

Rewards: A small negative reward (e.g., -1) for each step taken to encourage the agent to reach the goal.

Terminal States: Some grid cells (e.g., goal or dangerous zones) are terminal, meaning the episode ends when the agent enters these cells.

Objective: The goal is to find the optimal policy for reaching the terminal state with the highest reward.


✅ Summary of Differences
Method	Learns Value?	Improves    Policy? 	Speed			Notes
Policy Evaluation	✅	     ❌		Slow		Just computes values for a fixed policy
Policy Iteration	✅	     ✅		Medium		Alternates between evaluation & improvement
Value Iteration	        ✅	     ✅		Fastest		Combines both steps into one loop



🧪 Dynamic Programming Algorithms Used
1. Policy Iteration
"Iteratively improve your policy by checking how well it's doing, then making adjustments."

Policy Iteration alternates between two steps:

Policy Evaluation: Calculate the value of each state under the current policy. This step involves solving a set of equations to determine how much reward the agent expects to get from each state if it follows the current policy.

Policy Improvement: Using the value function from the previous step, update the policy to choose the best possible action for each state. This action is the one that maximizes the expected return.

Intuition:
Start with a random policy.

Evaluate how good it is.

Improve the policy based on the values.

Repeat until the policy stops changing — that’s the optimal policy!

2. Value Iteration
"Update values directly by considering the best possible future outcome for each state."

Value Iteration updates the value of each state iteratively until the values converge to the optimal ones. Unlike Policy Iteration, it combines the policy evaluation and policy improvement steps into one step.

Each update takes into account the best possible action (i.e., the one with the highest value) for each state, allowing it to converge quickly to the optimal policy.

Intuition:
Start by guessing values for all states.

For each state, consider all possible actions and update the value based on the best action (maximizing expected reward).

Repeat until the values stop changing.



📚 Reference
This project is based on:

Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.)
See Chapter 4 – Dynamic Programming for more information.