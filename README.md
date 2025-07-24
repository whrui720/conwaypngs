# Conway's Game of Life PNG Generator

This project generates a sequence of PNG images representing the evolution of Conway's Game of Life on predefined grid. Initializations can be set in csv format; one caveat is that additional padding of 0's (empty/dead cells) must exist if that specific cell, at any step, is alive. 

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. The PNG images for each generation will be saved in the `output` directory.

## Requirements

- Python 3.x
- numpy
- Pillow
