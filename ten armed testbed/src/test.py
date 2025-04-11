# import Bandit
import numpy as np
from tqdm import trange
import matplotlib
import matplotlib.pyplot as plt
import sys

sys.path.append(r"C:\Users\asus\Desktop\ReinforcementLearning\ten-armed-testbed")
matplotlib.use('Agg')


# f= Bandit()

print("hwl")

def simulate(runs, times, bandits):
    # region Summary
    """
    For any learning method, we can measure its performance and behavior as it improves with experience over 1000 time steps
    when applied to 1 of the bandit problems. This makes up 1 run. Repeating this for 2000 independent runs, each with a different
    bandit problem, we obtained measures of the learning algorithm’s average behavior.
    :param runs: Number of runs
    :param times: Number of times
    :param bandits: Bandit problems
    :return: Optimal action count mean and reward mean
    """
    # endregion Summary

    # region Body

    # Prepare a matrix filled with 0s for rewards
    rewards = np.zeros((len(bandits),runs, times))

    # Prepare a matrix filled with 0s for optimal action counts that has the same shape as rewards matrix
    optimal_action_counts = np.zeros(rewards.shape)

    # For every bandit
    for i, bandit in enumerate(bandits):
        # for every run
        for run in trange(runs):
            # initialize bandit
            bandit.initialize()

            # for every time step
            for time in range(times):
                # select an action
                action = bandit.act()

                # get the reward
                rewards[i, run, time] = bandit.step(action)

                # if the selected action is optimal for bandit
                if action == bandit.optimal_action:

                    # change the corresponding 0 in the optimal action counts matrix to 1
                    optimal_action_counts[i, run, time] = 1

    return  optimal_action_counts.mean(axis=1), rewards.mean(axis = 1)

    # endregion Body

# Plot an example reward distribution
plt.violinplot(dataset=np.random.randn(200, 10) + np.random.randn(10))
plt.title("Figure 2.1")
plt.xlabel("Action")
plt.ylabel("Reward distribution")
plt.savefig("../generated_images/figure_2_1.png")
plt.close()


# Create a list of epsilons with 0, 0.1 and 0.01 values
epsilions = [0, 0.1, 0.01]

# Create a list of bandits (1 bandit for every epsilon) where every bandit uses sample-average method
bandits = [Bandit(epsilon=epsilon, use_sample_averages=True) for epsilon in epsilions]

# Define number of runs
runs = 2000

# Define number of times
time = 1000

# Simulate optimal action counts and rewards
optimal_action_counts, rewards = simulate(runs, time, bandits)

 # Plotting
plt.figure(figsize=(10, 20))

plt.subplot(2, 1, 1)
for epsilon, rewards in zip(epsilions, rewards):
    plt.plot(rewards, label="$\epsilon = %.02f$" % epsilon)
plt.title("Figure 2.2")
plt.xlabel("Steps")
plt.ylabel("Average reward")
plt.legend()


plt.subplot(2, 1, 2)
for epsilon, counts in zip(epsilions, optimal_action_counts):
    plt.plot(counts, label="$\epsilon = %.02f$" % epsilon)
plt.xlabel("Steps")
plt.ylabel("% Optimal action")
plt.legend()

plt.savefig("../generated_images/figure_2_2.png")
plt.close()