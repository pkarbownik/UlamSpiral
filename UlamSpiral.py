import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime
import argparse

def generate_ulam_spiral(size):
    # Create a grid
    spiral = np.zeros((size, size), dtype=int)
    
    x, y = size // 2, size // 2  # Start in the middle of the grid
    num = 1
    
    # Directions for movement: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction_index = 0
    steps = 1  # Steps to take in the current direction
    
    while num <= size * size:
        for _ in range(2):
            for _ in range(steps):
                if num > size * size:
                    break
                spiral[y, x] = num
                x += directions[direction_index][0]
                y += directions[direction_index][1]
                num += 1
            direction_index = (direction_index + 1) % 4
        steps += 1
    
    return spiral

def plot_ulam_spiral(size, output_file):
    spiral = generate_ulam_spiral(size)
    prime_mask = np.vectorize(isprime)(spiral)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(prime_mask, cmap='Greys', interpolation='nearest')
    plt.title("Ulam Spiral")
    plt.axis('off')
    plt.savefig(output_file)
    print(f"Ulam spiral saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and plot an Ulam spiral of a given size.")
    parser.add_argument("-s", "--size", type=int, default=101, help="Size of the Ulam spiral (must be an odd number).")
    parser.add_argument("-o", "--output", type=str, default="ulam_spiral.png", help="Output file name for the plot.")
    args = parser.parse_args()
    
    if args.size % 2 == 0:
        print("Error: Size must be an odd number.")
    else:
        plot_ulam_spiral(args.size, args.output)
