import pygame
import random
import pygame.draw

pygame.init()   
WIDTH, HEIGHT = 500, 500

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the images
bomb_image = pygame.image.load("bomb.png")
diamond_image = pygame.image.load("dimond.png")

# Create the grid
grid = []
for i in range(5):
    row = []
    for j in range(5):
        if random.random() > 0.5:
            row.append(bomb_image)
        else:
            row.append(diamond_image)
    grid.append(row)

# Create the bet boxes
bet_boxes = []
for i in range(5):
    box = pygame.Rect(i * 100, HEIGHT - 50, 100, 25)
    bet_boxes.append(box)

# Create the bet button
bet_button = pygame.Rect(WIDTH - 100, HEIGHT - 50, 100, 25)

# Create the main loop
running = True
while running:
    # Update the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid
    for i in range(5):
        for j in range(5):
            image = grid[i][j]
            x = i * 100
            y = j * 100
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 100, 100))
            pygame.draw.blit(image, (x + 25, y + 25))

    # Draw the bet boxes
    for box in bet_boxes:
        pygame.draw.rect(screen, (255, 0, 0), box)

    # Draw the bet button
    pygame.draw.rect(screen, (0, 255, 0), bet_button)

    # Update the display
    pygame.display.update()
