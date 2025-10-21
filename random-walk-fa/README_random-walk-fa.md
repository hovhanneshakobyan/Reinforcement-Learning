Random Walk with Function Approximation
Overview

This project explores n-step Temporal Difference (TD) learning with function approximation, extending the classical Random Walk task from reinforcement learning.
It investigates how different feature representations — polynomial, Fourier, state aggregation, and tile coding — affect the stability, convergence, and accuracy of value estimation.

This concept is fundamental in reinforcement learning, prediction problems, and function approximation in continuous or large discrete spaces.

How It Works
Environment

Linear chain of states (e.g., 19 states)

Start from the center; move left or right with equal probability

Rewards:

−1 at left terminal

+1 at right terminal

0 otherwise

n-step TD Learning

The update uses the n-step return:

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

and

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
Function Approximation

The value function is approximated linearly:

𝑉
^
(
𝑠
)
=
𝑤
𝑇
𝑥
(
𝑠
)
V
^
(s)=w
T
x(s)

where 
𝑥
(
𝑠
)
x(s) is the feature vector.
Weights are updated by:

𝑤
←
𝑤
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
^
(
𝑆
𝑡
)
)
𝑥
(
𝑆
𝑡
)
w←w+α(G
t
(n)
	​

−
V
^
(S
t
	​

))x(S
t
	​

)
Feature Representations

Polynomial basis – simple nonlinear expansion

Fourier basis – smooth and flexible representation

State aggregation – coarse grouping of states

Tile coding – overlapping tilings for local generalization

Example Parameters
Parameter	Description	Example
num_states	Number of states	19
discount	γ (discount factor)	1.0
n_values	n-step values	[1, 2, 4, 8, 16]
alpha	Step size	0.01
basis	Feature type	"fourier"
order	Basis order	3
Files

random_walk_fa.py – Core TD learning and environment logic

bootstrapping.ipynb – n-step TD performance visualization

polynomials_vs_fourier.ipynb – Comparison of basis functions

state_aggregation.ipynb – Aggregation experiments

tile_coding.ipynb – Tile coding demonstration

requirements.txt – Dependencies

Results

Fourier basis converges faster and more smoothly

State aggregation improves stability but reduces precision

Higher n-step values balance bias and variance effectively

Summary

This project demonstrates how function approximation enables generalization in TD learning, bridging the gap between tabular and continuous-state reinforcement learning.
It highlights how feature selection and n-step updates shape learning performance and stability.