
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation


def generate_chladni_pattern(n, m, alpha=1.0, beta=1.0, resolution=500):
    """
    Generates a Chladni plate pattern based on resonant modes n and m.
    """
    # Create a 2D grid representing the plate surface
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    X, Y = np.meshgrid(x, y)

    # Chladni governing equation for a square plate
    Z = alpha * np.sin(n * np.pi * X) * np.sin(m * np.pi * Y) + \
        beta * np.sin(m * np.pi * X) * np.sin(n * np.pi * Y)

    # We want to simulate sand gathering at the nodal lines (where amplitude Z is close to 0)
    # Taking the absolute value helps us map the "quiet" zones easily
    nodal_lines = np.abs(Z)

    return nodal_lines


# --- Parameters to play with ---
# n and m represent the frequency modes. Higher numbers = more complex patterns.
n_mode = 6
m_mode = 2
alpha_coeff = 1.0
beta_coeff = -1.0  # Inverting beta often creates beautiful diagonal symmetries

# Generate the pattern
pattern = generate_chladni_pattern(n_mode, m_mode, alpha_coeff, beta_coeff)

# Plotting the result
plt.figure(figsize=(8, 8), facecolor='black')
# 'inferno', 'magma', or 'gray' work great for a "sand on a plate" look
plt.imshow(pattern, cmap='twilight_shifted', extent=[0, 1, 0, 1])
plt.axis('off')  # Hide axes for a clean art look
plt.title(f"Cymatic Pattern (Mode: {n_mode}, {m_mode})", color='white', fontsize=14)
plt.show()


# generate chaldni patterns
def generate_chaldni_pattern_3d(n):
    x = np.linspace(-np.pi, np.pi, 1000)
    y = np.linspace(-np.pi, np.pi, 1000)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(n*X)*np.sin(n*Y)
    plt.imshow(Z, cmap='gray')
    plt.show()
