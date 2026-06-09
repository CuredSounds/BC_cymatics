import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_chladni_pattern(n, m, alpha=1.0, beta=1.0, resolution=500):
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    x_grid, y_grid = np.meshgrid(x, y)

    pattern = (
        alpha * np.sin(n * np.pi * x_grid) * np.sin(m * np.pi * y_grid)
        + beta * np.sin(m * np.pi * x_grid) * np.sin(n * np.pi * y_grid)
    )

    return np.abs(pattern)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate cymatic-like Chladni plate visuals."
    )
    parser.add_argument("--n-mode", type=int, default=6, help="First mode number.")
    parser.add_argument("--m-mode", type=int, default=2, help="Second mode number.")
    parser.add_argument(
        "--alpha", type=float, default=1.0, help="Coefficient for the first term."
    )
    parser.add_argument(
        "--beta", type=float, default=-1.0, help="Coefficient for the second term."
    )
    parser.add_argument(
        "--resolution", type=int, default=500, help="Grid resolution for the plate."
    )
    parser.add_argument(
        "--cmap", default="twilight_shifted", help="Matplotlib colormap name."
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional image path to save instead of only displaying the figure.",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the figure interactively after generating it.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.show and not args.output:
        raise SystemExit("Use --show to display the figure or --output to save it.")

    pattern = generate_chladni_pattern(
        args.n_mode,
        args.m_mode,
        alpha=args.alpha,
        beta=args.beta,
        resolution=args.resolution,
    )

    fig = plt.figure(figsize=(8, 8), facecolor="black")
    plt.imshow(pattern, cmap=args.cmap, extent=[0, 1, 0, 1])
    plt.axis("off")
    plt.title(
        f"Cymatic Pattern (Mode: {args.n_mode}, {args.m_mode})",
        color="white",
        fontsize=14,
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.output, bbox_inches="tight", facecolor=fig.get_facecolor())

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
