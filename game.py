import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (0, 0, 0)

# Set the snake's starting position and size
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_size = 10

# Set the snake's starting direction
snake_dx = 0
snake_dy = 1

# Set the food's starting position
food_x = random.randint(0, screen_width - snake_size)
food_y = random.randint(0, screen_height - snake_size)

# Set the game's state
game_state = "running"

# Set the game's score
score = 0

# Set the game's font
font = pygame.font.SysFont("Arial", 20)

# Main game loop
while game_state == "running":
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "quit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = 1
            elif event.key == pygame.K_LEFT:
                snake_dx = -1
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = 1
                snake_dy = 0

    # Move the snake
    snake_x += snake_dx * snake_size
    snake_y += snake_dy * snake_size

    # Check if the snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        # Increase the snake's length
        snake_size += 1

        # Set the food's new position
        food_x = random.randint(0, screen_width - snake_size)
        food_y = random.randint(0, screen_height - snake_size)

        # Increase the score
        score += 1

    # Check if the snake has collided with itself
    for i in range(1, snake_size):
        if snake_x == snake_x - i * snake_dx and snake_y == snake_y - i * snake_dy:
            game_state = "over"

    # Check if the snake has collided with the walls
    if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
        game_state = "over"

    # Draw the screen
    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 255, 255), (snake_x, snake_y, snake_size, snake_size))
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_size, snake_size))
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()

# Game over screen
if game_state == "over":
    screen.fill(background_color)
    text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(text, (screen_width / 2 - 50, screen_height / 2 - 10))
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (screen_width / 2 - 50, screen_height / 2 + 10))
    pygame.display.update()

    # Wait for the player to press a key
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset the game
                    snake_x = screen_width / 2
                    snake_y = screen_height / 2
                    snake_size = 10
                    snake_dx = 0
                    snake_dy = 1
                    food_x = random.randint(0, screen_width - snake_size)
                    food_y = random.randint(0, screen_height - snake_size)
                    score = 0
                    game_state = "running"
                    break

# Quit pygame
pygame.quit()
