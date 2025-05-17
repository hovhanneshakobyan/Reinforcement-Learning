📘 Overview
This project brings to life the Cliff Walking example from Reinforcement Learning: An Introduction by Sutton & Barto (2nd Edition, Chapter 6).

It demonstrates how agents can learn online, from raw experience, without waiting for entire episodes to finish — using Temporal-Difference (TD) methods like:

SARSA (on-policy TD control)

Q[s,a] ← Q[s,a] + α * ( r + γ * Q[s',a'] - Q[s,a] )

Q-learning (off-policy TD control)

Q[s,a] ← Q[s,a] + α * ( r + γ * max_{a'} Q[s',a'] - Q[s,a] )

Expected SARSA (a hybrid of the two)

Q[s,a] ← Q[s,a] + α * ( r + γ * E_{a'}[Q[s',a']] - Q[s,a] )


🕹️ The Environment: Cliff Walking Gridworld
Imagine a grid where the agent starts on one side and needs to reach a goal — but there’s a cliff in the middle. If the agent steps into it, it “falls,” receiving a heavy negative reward and restarting from the beginning.

🔲 Grid size: 4 rows × 12 columns

🚶 Start: Bottom-left

🎯 Goal: Bottom-right

🕳️ Cliff: Bottom row between start and goal

⏱️ Episodic: The agent restarts after falling or reaching the goal

📉 Rewards:

Regular move: -1

Falling off the cliff: -100

🎯 Learning Objectives
Learn how an agent can avoid falling off the cliff using trial and error.

Compare how different TD algorithms learn different policies.

Understand the role of on-policy vs off-policy learning.

🧠 How the Algorithms Work (In Plain Terms)
🔁 SARSA (On-Policy)
“I learn from the actions I actually take.”

SARSA updates its behavior based on the path it really followed — including its mistakes. If it explores dangerously (like walking near the cliff), it learns from those risky actions. This often leads to safer policies, as it tends to avoid places where it had bad experiences.

🔀 Q-learning (Off-Policy)
“I learn from the best move I could have made.”

Q-learning imagines what would have happened if it had taken the best possible action at each step, even if it didn’t actually do that. This helps it learn the optimal policy faster, but it may hug the cliff more closely because it assumes it will always act perfectly.

🧮 Expected SARSA
“I learn from what I expect to do, considering all possibilities.”

Expected SARSA looks ahead and averages over all possible next moves, based on how likely each one is. This gives it a smoother, more stable learning process — not too optimistic (like Q-learning), not too reactive (like SARSA), but somewhere in between.