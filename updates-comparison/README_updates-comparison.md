Updates Comparison – Expected vs. Sample Updates
Overview

This project compares expected updates and sample updates in value estimation, analyzing how computation cost vs. accuracy scales with the branching factor (b).
It addresses the key question:

“Is it better to perform one expensive expected update or many cheaper sample updates?”

Where It’s Used

Used in reinforcement learning to understand efficiency trade-offs in planning and value function estimation — foundational to algorithms like Q-learning and SARSA.

Files

expectation_vs_sample.py – Implements calculate_errors(branching_factor) to compute RMSE for various branching factors.

expectation_vs_sample.ipynb – Simulates expected vs. sample updates for b ∈ {2, 10, 100, 1000} and visualizes convergence.

requirements.txt – Dependencies.

README.md – Documentation.

How It Works

Expected update:

𝑄
(
𝑠
,
𝑎
)
←
∑
𝑠
′
𝑝
(
𝑠
′
∣
𝑠
,
𝑎
)
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
]
Q(s,a)←
s
′
∑
	​

p(s
′
∣s,a)[r+γ
a
′
max
	​

Q(s
′
,a
′
)]

Accurate but requires evaluating b next states.

Sample update:

𝑄
(
𝑠
,
𝑎
)
←
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
Q(s,a)←r+γ
a
′
max
	​

Q(s
′
,a
′
)

Cheaper — updates using one sampled transition, introducing noise but scaling better for large b.

Simulation Steps:

Generate random next-state values (∼ N(0, 1))

Compute true expected value

Iteratively sample and update

Repeat 100 runs and average RMSE

Parameters
branching_factors = [2, 10, 100, 1000]
runs = 100
samples_per_run = 2 * branching_factor

Results

X-axis: Computation (normalized by b)

Y-axis: RMS error in value estimates

Findings:

Small b → expected updates more accurate

Large b → sample updates achieve similar accuracy faster

Sampling scales better — ideal for large environments

Summary

Expected updates = accurate but costly
Sample updates = noisy but efficient
→ In large-scale RL, sample-based methods dominate, forming the foundation of modern learning algorithms.