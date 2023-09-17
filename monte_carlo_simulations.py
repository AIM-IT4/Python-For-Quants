
import numpy as np
import matplotlib.pyplot as plt

# Basics of Monte Carlo
def monte_carlo_estimation_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = np.random.uniform(-1, 1, 2)
        distance_to_origin = x**2 + y**2
        if distance_to_origin <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

estimated_pi = monte_carlo_estimation_pi(100000)
print(f"Estimated value of pi using Monte Carlo: {estimated_pi}")
