import numpy as np
import csv

def create_koks_galaxy_csv(filepath, grid_size=25):
  """Create a CSV file with Kok's Galaxy centered in a grid."""
  grid = np.zeros((grid_size, grid_size), dtype=int)

  # Kok's Galaxy pattern
  koks_galaxy = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
  ]

  # Center the pattern in the grid
  start_x = (grid_size - len(koks_galaxy)) // 2
  start_y = (grid_size - len(koks_galaxy[0])) // 2

  for i, row in enumerate(koks_galaxy):
    for j, cell in enumerate(row):
      grid[start_x + i, start_y + j] = cell

  # Save to CSV
  with open(filepath, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grid)

def main():
  create_koks_galaxy_csv("koks_galaxy.csv")

if __name__ == "__main__":
  main()