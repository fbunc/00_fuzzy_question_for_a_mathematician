import pygame
import numpy as np
import colorsys
from PIL import Image, ImageOps
import os

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the grid cells
CELL_SIZE = 1im

# Placeholder values for ROWS and COLS, will be updated after loading the image
ROWS, COLS = 100, 160

# Set the maximum resolution for the image to avoid performance issues
MAX_RESOLUTION = (800, 600)

# Create the frames directory if it doesn't exist
if not os.path.exists('frames'):
    os.makedirs('frames')

# Load and process the image
def load_image(image_path):
    global ROWS, COLS, grid
    image = Image.open(image_path).convert('L')  # Convert image to grayscale
    image.thumbnail(MAX_RESOLUTION, Image.ANTIALIAS)  # Resize image to fit within max resolution
    COLS, ROWS = image.size
    image = ImageOps.pad(image, (COLS, ROWS))  # Ensure the image fits the grid
    image_data = np.array(image)
    
    # Initialize grid based on image data (0 for black, 1 for white)
    grid = np.where(image_data > 128, 1, 0)

# Function to update the window size based on the grid size
def update_window_size():
    global WINDOW_SIZE, window
    WINDOW_SIZE = (COLS * CELL_SIZE, ROWS * CELL_SIZE)
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Conway's Game of Life")

# Function to clear the grid
def clear_grid():
    global grid
    grid = np.zeros((ROWS, COLS), dtype=int)

# Function to update the display
def update_display():
    pygame.display.flip()

# Function to save the current frame
frame_counter = 0
def save_frame():
    global frame_counter
    pygame.image.save(window, f'frames/frame_{frame_counter:04d}.png')
    frame_counter += 1

# Get the image file name from the user
image_file = input("Enter the image file name (e.g., input_image.png): ")

# Load the image
load_image(image_file)
update_window_size()

# Game loop
running = True
initial_pattern = True  # Start with the initial pattern loaded from the image

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Clear the grid and restart
                initial_pattern = False
                clear_grid()
                update_display()
            elif event.key == pygame.K_r:
                # Reload the image as the initial pattern
                load_image(image_file)
                initial_pattern = True

    if initial_pattern:
        # Create a copy of the grid to store the next generation
        new_grid = np.copy(grid)

        # Update each cell in the grid
        for i in range(ROWS):
            for j in range(COLS):
                # Get the indices of the neighboring cells
                neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                             (i, j - 1), (i, j + 1),
                             (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

                # Count the number of live neighbors
                live_neighbors = 0
                for neighbor in neighbors:
                    if neighbor[0] in range(ROWS) and neighbor[1] in range(COLS):
                        if grid[neighbor[0], neighbor[1]] == 1:
                            live_neighbors += 1

                # Apply the rules of Conway's Game of Life
                if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_grid[i, j] = 0
                elif grid[i, j] == 0 and live_neighbors == 3:
                    new_grid[i, j] = 1

        # Update the grid with the new generation
        grid = np.copy(new_grid)

        # Save the current frame
        save_frame()

    # Clear the game window
    window.fill(BLACK)

    # Draw the cells
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i, j] == 1:
                # Calculate the cell position in the game window
                x = j * CELL_SIZE
                y = i * CELL_SIZE

                # Calculate the angle of the cell with respect to the center of the game canvas
                center_x = WINDOW_SIZE[0] // 2
                center_y = WINDOW_SIZE[1] // 2
                dx = x - center_x
                dy = y - center_y
                angle = np.arctan2(dy, dx)

                # Map the angle to a hue value in the range [0, 360]
                hue = (np.degrees(angle) + 180) % 360

                # Set the saturation and lightness values
                saturation = 100
                lightness = 50

                # Convert the HSL color values to RGB
                rgb = colorsys.hls_to_rgb(hue / 360, lightness / 100, saturation / 100)
                color = tuple(int(component * 255) for component in rgb)

                # Draw the cell with the calculated color
                pygame.draw.rect(window, color, (x, y, CELL_SIZE, CELL_SIZE))

    # Update the display
    update_display()

# Quit the game
pygame.quit()
