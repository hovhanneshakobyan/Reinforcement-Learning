Windy Gridworld – A Reinforcement Learning Example 🌬️🏞️
What is the Windy Gridworld? 🧭
The Windy Gridworld is a popular Reinforcement Learning (RL) environment used to demonstrate fundamental RL concepts such as exploration vs. exploitation, state transitions, and policy evaluation. It’s a variation of the classic Gridworld, but with a twist: wind! 🌬️

In this environment, the agent must navigate through a grid, trying to reach a goal state. However, the challenge comes from the wind that pushes the agent off course, making it harder to get to the goal. This introduces stochasticity, meaning that the outcome of the agent’s actions is not deterministic — the wind plays a major role in the agent’s movement.

Grid Setup 🔲
Grid Size: Typically, the grid is a 7x10 layout (7 rows and 10 columns).

Start Position: The agent begins at the bottom-left corner (position 0,0).

Goal Position: The goal is typically at the top-right corner (position 3,7).

Wind: Each column of the grid has varying wind strength, which affects how much the agent’s movement is pushed up or down.

State Space 🔢
The environment consists of states represented by the position of the agent within the grid. The states can be visualized as a 2D array, where each position is a unique state.

Example Grid:
Let’s visualize the grid with the wind effects on each column:

css
Копировать
Редактировать
   0  1  2  3  4  5  6  7  8  9
0 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
1 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
3 [ 1, 1, 2, 2, 2, 1, 1, 0, -1, -1]
4 [ 1, 1, 2, 2, 2, 1, 1, 0, -1, -1]
5 [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
6 [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
The wind strength in each column varies:

Column 0: No wind

Column 1-2: Wind blows up by 1

Column 3-5: Wind blows up by 2

Column 6-7: Wind blows down by 1

Column 8-9: Wind blows down by 2

Action Space 🎮
At each state, the agent can choose one of the following actions:

Up (U): Move up by one row (affected by wind).

Down (D): Move down by one row (affected by wind).

Left (L): Move left by one column.

Right (R): Move right by one column.

The agent must consider how the wind will affect its movement, making it more challenging to follow the optimal path.

Reward Function 🎯
The reward structure in Windy Gridworld typically follows these rules:

Goal Reached: The agent receives a +1 reward when it reaches the goal state.

Penalty for Each Step: The agent receives a -1 penalty for each step it takes to encourage the shortest path.

Other States: All other states have a reward of 0.

The agent’s objective is to learn the optimal policy that maximizes cumulative rewards by reaching the goal while avoiding the penalties of wandering off course due to wind.

Challenges in Windy Gridworld ⚖️
Stochastic Transitions: The wind introduces uncertainty, making the agent’s state transitions unpredictable.

Exploration vs. Exploitation: The agent must balance exploration (trying new actions) with exploitation (sticking to known, successful actions).

Delayed Rewards: The agent doesn’t always know the immediate reward after each action, making it harder to determine which actions will lead to the goal.

This makes the Windy Gridworld a great environment to experiment with Reinforcement Learning algorithms.