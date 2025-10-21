Square Wave Function Approximation – Feature-Based Value Estimation
Overview

This project demonstrates feature-based value function approximation, a core concept used in reinforcement learning and function estimation for representing continuous or complex state spaces.
It approximates a discontinuous square wave using overlapping feature intervals and online gradient descent.

How It Works

Target function:

𝑓
(
𝑥
)
=
1
f(x)=1 if 
0.5
<
𝑥
<
1.5
0.5<x<1.5; 
𝑓
(
𝑥
)
=
0
f(x)=0 otherwise
Domain: [0, 2)

Approximation model:
The domain is divided into overlapping feature windows.
Each active feature contributes a weight 
𝑤
𝑖
w
i
	​

:

𝑣
^
(
𝑥
)
=
∑
𝑖
∈
𝑎
𝑐
𝑡
𝑖
𝑣
𝑒
(
𝑥
)
𝑤
𝑖
v
^
(x)=
i∈active(x)
∑
	​

w
i
	​


Learning rule:

𝑤
𝑖
←
𝑤
𝑖
+
𝛼
⋅
(
𝑓
(
𝑥
)
−
𝑣
^
(
𝑥
)
)
/
𝑛
𝑎
𝑐
𝑡
𝑖
𝑣
𝑒
w
i
	​

←w
i
	​

+α⋅(f(x)−
v
^
(x))/n
active
	​


where α is the learning rate and n_active is the number of active features.

Parameters
Parameter	Description	Default
feature_width	Width of each feature window	0.1
step_size	Learning rate	0.2
num_of_features	Number of overlapping features	50
domain	Input space	[0.0, 2.0]
Files

square_wave.py – Main training script

classes.py – Defines Interval and ValueFunction classes

square_wave.ipynb – Notebook for visualization and experiments

requirements.txt – Project dependencies

Results

The model learns to approximate the square wave by adjusting weights of active features.
Overlapping intervals allow smooth approximation even near discontinuities.

Applications

Value function estimation in Reinforcement Learning

Continuous state approximation

Simple online learning demonstration