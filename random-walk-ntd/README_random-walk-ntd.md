Random Walk: n-step Temporal Difference Learning
Overview

This project implements the Random Walk environment to study n-step Temporal Difference (TD) learning, a core algorithm in reinforcement learning.
An agent starts from the center of a 19-state chain and learns to estimate state values based on returns over n future steps, analyzing the bias–variance trade-off as n varies.

How It Works
Environment

States: 19 non-terminal states + 2 terminal states

Start: center of the chain

Transitions: move left or right with probability 0.5

Rewards:

−1 at the left terminal

+1 at the right terminal

0 otherwise

n-step TD Learning

For each state:

𝐺
𝑡
(
𝑛
)
=
∑
𝑘
=
0
𝑛
−
1
𝛾
𝑘
𝑅
𝑡
+
𝑘
+
1
+
𝛾
𝑛
𝑉
(
𝑆
𝑡
+
𝑛
)
G
t
(n)
	​

=
k=0
∑
n−1
	​

γ
k
R
t+k+1
	​

+γ
n
V(S
t+n
	​

)
𝑉
(
𝑆
𝑡
)
←
𝑉
(
𝑆
𝑡
)
+
𝛼
 
(
𝐺
𝑡
(
𝑛
)
−
𝑉
(
𝑆
𝑡
)
)
V(S
t
	​

)←V(S
t
	​

)+α(G
t
(n)
	​

−V(S
t
	​

))

Smaller n → more bias, less variance

Larger n → less bias, more variance

Example Parameters
Parameter	Description	Example
states_number	Number of non-terminal states	19
discount	Discount factor (γ)	1.0
steps	n-step values	1, 2, 4, 8, ...
step_sizes	Learning rates (α)	0.0–1.0
episodes	Episodes per run	10
runs	Independent runs	100
Files

random_walk.py – Environment setup and n-step TD updates

random_walk.ipynb – Simulations, RMSE evaluation, and plots

requirements.txt – Dependencies

Results

Visualizes learning curves for different n values

Compares RMSE over episodes against the true state values

Demonstrates the bias–variance trade-off in n-step TD learning

Summary

This project illustrates how n-step TD methods bridge the gap between Monte Carlo and TD(0) learning, offering insight into how multi-step updates influence learning speed and stability in reinforcement learning environments.