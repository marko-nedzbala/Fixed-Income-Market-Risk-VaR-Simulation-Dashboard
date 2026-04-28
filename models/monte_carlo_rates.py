import numpy as np

def simulate_rate_paths(n_sims=1000, n_steps=252, r0=0.03, mu=0.0, sigma=0.01):
    dt = 1/252
    paths = np.zeros((n_sims, n_steps))

    for i in range(n_sims):
        rates = [r0]
        for t in range(1, n_steps):
            dr = mu * dt + sigma * np.sqrt(dt) * np.random.normal()
            rates.append(max(rates[-1] + dr, 0))
        paths[i] = rates

    return paths