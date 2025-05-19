import numpy as np
import pandas as pd
import ace_tools as tools

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Cases with appropriate mass values and force estimation
cases = [
    ("Worker pushing a wooden crate", (50, 200), (200, 600)),
    ("Dog pulling a small sled", (10, 30), (50, 200)),
    ("Person dragging a backpack with wheels", (5, 20), (100, 300)),
    ("Child pushing a toy truck", (2, 10), (50, 150)),
    ("Farmer pulling a plow with an ox", (100, 300), (500, 1500)),
    ("Robot arm pushing a box", (20, 100), (200, 800)),
    ("Person dragging a kayak", (30, 80), (100, 400)),
    ("Car towing a trailer", (500, 2000), (3000, 10000)),
    ("Construction worker pushing a wheelbarrow", (40, 150), (200, 800)),
    ("Bulldozer pushing a pile of dirt", (1000, 5000), (5000, 20000)),
]

valid_cases = []

# Iterate until we get valid values
for case, mass_range, force_range in cases:
    while True:
        mu_k = np.random.uniform(0.1, 0.9)  # Coefficient of kinetic friction
        theta = np.random.uniform(10, 60)  # Angle in degrees

        # Determine if force is upwards or downwards
        if "pulling" in case or "dragging" in case or "towing" in case:
            theta = np.random.uniform(10, 60)  # Upwards angle
        else:
            theta = np.random.uniform(-60, -10)  # Downwards angle

        M = np.random.uniform(mass_range[0], mass_range[1])  # Mass of the object
        max_force = np.random.uniform(force_range[0], force_range[1])  # Maximum force

        # Convert theta to radians
        theta_rad = np.radians(theta)

        # Calculate the force required
        F = (mu_k * M * g) / (np.cos(theta_rad) + mu_k * np.sin(theta_rad))

        # Validate the force
        if 0 < F < max_force:
            valid_cases.append((case, round(mu_k, 2), round(theta, 2), round(M, 2), round(F, 2), round(max_force, 2)))
            break

# Create DataFrame and display
df = pd.DataFrame(valid_cases, columns=["Scenario", "μ_k", "θ (deg)", "Mass (kg)", "Required Force (N)", "Max Available Force (N)"])
tools.display_dataframe_to_user(name="Valid Force Calculation Cases", dataframe=df)
