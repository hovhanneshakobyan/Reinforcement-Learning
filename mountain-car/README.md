# 🚗 Mountain Car – Semi-Gradient *n-Step SARSA* with Tile Coding

This project implements **Semi-Gradient n-Step SARSA** with **tile coding** on the classic **Mountain Car** reinforcement learning problem.
It reproduces and extends the experiments from *Sutton & Barto (2018), “Reinforcement Learning: An Introduction,”* Chapter 10 — Figures 10.1 – 10.4.

---

## 🧠 Background

The **Mountain Car** task is a continuous-state control problem:

* **Goal:** drive the car to the top of the hill (position ≥ 0.5).
* **State:**

  * Position ∈ [ −1.2 , 0.5 ]
  * Velocity ∈ [ −0.07 , 0.07 ]
* **Actions:**

  * −1 → push left
  * 0  → no push
  * +1 → push right
* **Reward:** −1 at each step until the goal is reached.

Because the car’s engine is too weak to climb directly, it must first back up to gain momentum — making it an ideal benchmark for temporal-difference control algorithms with function approximation.

---

## ⚙️ Algorithm Overview

### 🔹 Semi-Gradient *n-Step SARSA*

An on-policy TD control algorithm that updates the action-value function Q(s, a) using *n-step returns*.

**Update target:**

[
G_t^{(n)} = R_{t+1} + R_{t+2} + \dots + R_{t+n} + Q(S_{t+n}, A_{t+n})
]

**Weight update:**

[
\mathbf{w} \leftarrow \mathbf{w} + \alpha \big( G_t^{(n)} - \hat{Q}(S_t, A_t; \mathbf{w}) \big) \nabla_\mathbf{w} \hat{Q}(S_t, A_t; \mathbf{w})
]

When *n = 1*, this reduces to standard one-step SARSA.

---

### 🔹 Tile Coding (Function Approximation)

Tile coding discretizes continuous variables into overlapping *tilings*.

Each tiling produces one active feature for a given (state, action), and the estimated value is the sum of the corresponding weights.

Advantages:

* Efficient linear approximation
* Generalization across nearby states
* Fast and sparse updates

---

## 🧩 Project Structure

```
├── src/
│   ├── mountain_car.py     # Environment, n-step SARSA, plotting utilities
│   └── tile_coding.py      # Sutton's tile coding implementation (IHT, tiles)
├── book_images/            # Reference figures from Sutton & Barto
├── generated_images/       # Output of trained runs (Figures 10.1–10.4)
└── README.md
```

---

## 📦 Requirements

**Python ≥ 3.8**

Install dependencies:

```bash
pip install numpy matplotlib tqdm ipython
```

Optional (for interactive work):

```bash
pip install jupyterlab
```

---

## 🚀 How to Run

### 1️⃣ Train and Visualize Learning

```bash
python src/mountain_car.py
```

This script will:

* Run 9 000 episodes of training.
* Plot the **cost-to-go** surface at selected episodes (Figure 10.1).
* Compare learning curves for different step-sizes (Figure 10.2).
* Compare 1-step vs 8-step SARSA (Figure 10.3).
* Explore the combined effect of α and n (Figure 10.4).

Results are saved automatically in:

```
/generated_images/
```

---

## 📊 Output Figures

|      Figure     | Description                                   |
| :-------------: | :-------------------------------------------- |
| **Figure 10.1** | Evolution of cost-to-go surface over training |
| **Figure 10.2** | Learning curves for various step sizes α      |
| **Figure 10.3** | Comparison of n = 1 vs n = 8 SARSA            |
| **Figure 10.4** | Combined effect of α and n on learning speed  |

Each corresponds directly to examples from Sutton & Barto (2018).

---

## 🧩 Key Classes and Functions

| Name                                             | Purpose                                      |
| ------------------------------------------------ | -------------------------------------------- |
| `ValueFunction`                                  | Linear value approximator using tile coding  |
| `get_action(position, velocity, value_function)` | ε-greedy policy for action selection         |
| `step(position, velocity, action)`               | Physics simulation of the car                |
| `semi_gradient_n_step_sarsa(value_function, n)`  | Core training loop implementing n-step SARSA |
| `print_cost(value_function, episode, ax)`        | 3D visualization of cost-to-go surface       |

---

## 📈 Core Parameters

| Parameter        | Description                      | Typical Value        |
| ---------------- | -------------------------------- | -------------------- |
| `num_of_tilings` | Number of overlapping tilings    | 8                    |
| `step_size (α)`  | Learning rate divided by tilings | 0.3 / num_of_tilings |
| `n_steps`        | Number of bootstrapping steps    | 1 or 8               |
| `episodes`       | Training iterations              | 9 000 (max)          |

---

## 🔍 Research Context and Use Cases

This project demonstrates:

* Function approximation with **tile coding**
* **n-step bootstrapping** vs 1-step methods
* The impact of **α (step-size)** and **n (update horizon)**
* Continuous-state control with **TD learning**

It’s valuable for:

* Reproducing textbook results for study or teaching
* Experimenting with multi-step TD methods
* Serving as a baseline for extensions such as:

  * Eligibility traces (λ)
  * Off-policy variants (e.g. Q(σ))
  * Actor–Critic algorithms

---

## 📚 References

1. Sutton, R. S., & Barto, A. G. (2018).
   *Reinforcement Learning: An Introduction (2nd Edition).* MIT Press.
   [http://incompleteideas.net/book/the-book.html](http://incompleteideas.net/book/the-book.html)

2. Mountain Car environment (Example 10.1 – 10.4).



> *“Generalization is the crux of learning — tile coding makes it possible for continuous worlds.”*
> — Sutton & Barto (2018)
