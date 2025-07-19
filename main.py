import numpy as np
from PIL import Image
import os
import datetime
import csv

def initialize_grid(size):
    """Initialize a size x size grid with random 0s and 1s."""
    return np.random.choice([0, 1], size=(size, size))

def load_grid_from_csv(filepath):
    """Load a grid from a CSV file."""
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        grid = [list(map(int, row)) for row in reader]
    return np.array(grid)

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

def save_grid_as_png(grid, generation, output_dir, upscale_resolution=1920):
    """Save the grid as a PNG image with a transparent background and radial opacity."""
    scale = upscale_resolution // grid.shape[0]  # Calculate the scale factor
    upscale_size = (grid.shape[1] * scale, grid.shape[0] * scale)
    img = Image.new("RGBA", upscale_size, (0, 0, 0, 0))  # Transparent background

    # Calculate the center of the grid
    center_x, center_y = grid.shape[0] // 2, grid.shape[1] // 2
    max_distance = np.sqrt(center_x**2 + center_y**2)  # Maximum possible distance from the center

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == 1:
                # Calculate the distance from the center
                distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
                # Avoid division by zero
                if max_distance > 0:
                    # Adjust the opacity to make the gradient more obvious
                    opacity = int(255 * ((1 - distance / max_distance) ** 1.5))  # Squared for stronger gradient
                else:
                    opacity = 255  # Full opacity if max_distance is zero
                # Ensure opacity is within valid bounds
                opacity = max(0, min(255, opacity))
                # Fill the entire cell block with the same opacity
                for dx in range(scale):
                    for dy in range(scale):
                        img.putpixel((y * scale + dy, x * scale + dx), (255, 255, 255, opacity))  # White with uniform opacity
    img.save(os.path.join(output_dir, f"file-{generation}.png"))

def main():
    size = 25
    generations = 8

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join("output", f"sequence_{timestamp}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Choose between random initialization or loading from a CSV
    use_csv = input("Load grid from CSV? (y/n): ").strip().lower() == 'y'
    if use_csv:
        csv_path = input("Enter the path to the CSV file: ").strip()
        grid = load_grid_from_csv(csv_path)
    else:
        grid = initialize_grid(size)

    for generation in range(generations):
        save_grid_as_png(grid, generation, output_dir)
        grid = next_generation(grid)

if __name__ == "__main__":
    main()
