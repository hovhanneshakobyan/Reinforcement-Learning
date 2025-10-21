Maze Navigation – Dyna-Q, Dyna-Q+, and Prioritized Sweeping
Overview

This project explores model-based reinforcement learning through the Dyna architecture, applied to a maze navigation problem.
It compares three algorithms commonly used in planning and decision-making tasks:

Dyna-Q — classical model-based reinforcement learning

Dyna-Q+ — adds time-based exploration bonuses for better adaptability

Prioritized Sweeping — focuses planning on high-priority state–action updates

These methods are widely used in autonomous navigation, robot path planning, and simulation-based reinforcement learning research.

How It Works
Environment

Grid world: 6×9

Start: (2, 0), Goal: (0, 8)

Obstacles block certain cells; the maze can change mid-training

Rewards: +1 for reaching the goal, 0 otherwise

Transitions are deterministic

Algorithms

Dyna-Q
Combines real experience and simulated model-based planning:

𝑄
(
𝑠
,
𝑎
)
←
𝑄
(
𝑠
,
𝑎
)
+
𝛼
[
𝑟
+
𝛾
max
⁡
𝑎
′
𝑄
(
𝑠
′
,
𝑎
′
)
−
𝑄
(
𝑠
,
𝑎
)
]
Q(s,a)←Q(s,a)+α[r+γ
a
′
max
	​

Q(s
′
,a
′
)−Q(s,a)]

Dyna-Q+
Adds a time-based exploration bonus:

𝑟
′
=
𝑟
+
𝜅
⋅
𝑡
−
𝜏
(
𝑠
,
𝑎
)
r
′
=r+κ⋅
t−τ(s,a)
	​


Prioritized Sweeping
Uses a priority queue to update the most important transitions first.

Key Parameters
Parameter	Description	Example
discount (γ)	Discount factor	0.95
step_size (α)	Learning rate	0.1
exploration_probability (ε)	ε-greedy policy	0.1
time_weight (κ)	Dyna-Q+ exploration bonus	1e-4
planning_steps	Number of simulated updates	5
threshold (θ)	Priority threshold	0.01
runs	Averaged training runs	10
Files

maze.py – Maze environment and state transitions

models.py – Environment models for Dyna-Q, Dyna-Q+, and Prioritized Sweeping

functions.py – Core algorithm logic

dyna.py – Parameter configuration (DynaParams)

dyna_maze.ipynb – Dyna-Q vs Dyna-Q+ training visualization

changing_maze.ipynb – Adaptation to maze changes

prioritized_sweeping.ipynb – Efficient planning demonstration

requirements.txt – Dependencies

Results

Dyna-Q: Fast initial learning but struggles when the environment changes.

Dyna-Q+: Adapts faster to new obstacles using exploration bonuses.

Prioritized Sweeping: Achieves efficient learning with fewer model updates.

Summary

These experiments show how model-based planning, exploration bonuses, and priority-driven updates accelerate learning and adaptability in reinforcement learning systems.
They highlight the trade-off between exploration, efficiency, and computational cost in dynamic environments.