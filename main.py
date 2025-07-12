import numpy as np
from PIL import Image
import os

def initialize_grid(size):
    """Initialize a 100x100 grid with random 0s and 1s."""
    return np.random.choice([0, 1], size=(size, size))

def count_neighbors(grid, x, y):
    """Count the number of alive neighbors for a cell."""
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            count += grid[nx, ny]
    return count

def next_generation(grid):
    """Compute the next generation of the grid."""
    new_grid = np.zeros_like(grid)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            alive_neighbors = count_neighbors(grid, x, y)
            if grid[x, y] == 1 and alive_neighbors in [2, 3]:
                new_grid[x, y] = 1
            elif grid[x, y] == 0 and alive_neighbors == 3:
                new_grid[x, y] = 1
    return new_grid

def save_grid_as_png(grid, generation, output_dir):
    """Save the grid as a PNG image."""
    img = Image.fromarray((grid * 255).astype(np.uint8))
    img.save(os.path.join(output_dir, f"generation_{generation:04d}.png"))

def main():
    size = 100
    generations = 100
    output_dir = "output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    grid = initialize_grid(size)

    for generation in range(generations):
        save_grid_as_png(grid, generation, output_dir)
        grid = next_generation(grid)

if __name__ == "__main__":
    main()
