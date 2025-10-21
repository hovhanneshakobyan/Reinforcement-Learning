Trajectory Sampling – Expected vs. On-Policy Updates
Overview

This project compares uniform sampling and on-policy sampling in planning with expected one-step updates.
It explores how different update distributions affect learning speed, policy quality, and the focus vs. coverage trade-off in reinforcement learning.

Where It’s Used

This concept is mainly used in model-based reinforcement learning and planning algorithms such as Dyna-Q, where the agent uses simulated experience to improve value estimates.

Files

trajectory_sampling.py – Defines the environment and implements:

uniform_sampling() – evenly updates all state–action pairs

on_policy_sampling() – updates based on on-policy visitation

evaluate_policy() – Monte Carlo policy evaluation

run_experiment() – runs both methods with multiprocessing

trajectory_sampling.ipynb – Runs experiments, plots results, and compares performance.

requirements.txt – Dependencies.

README.md – Project documentation.

How It Works

Each experiment defines a random episodic MDP with:

Two actions per state

Termination probability = 0.1

Rewards ∼ N(0,1)

Uniform sampling: evenly updates all state–action pairs → better long-term accuracy.
On-policy sampling: focuses on frequently visited pairs → faster early learning.

Parameters
actions = [0, 1]
termination_probability = 0.1
max_steps = 20000
exploration_probability = 0.1
num_states = [1000, 10000]
branch_factors = [1, 3, 10]

Results

Plots show the value of the start state vs. computation time.

On-policy sampling learns faster early on.

Uniform sampling surpasses later with better overall accuracy.

Summary

This project highlights how sampling distribution influences convergence in planning-based RL — balancing efficiency (on-policy) and completeness (uniform) for optimal learning performance.