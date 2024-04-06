
import pygame
import sys
import random

# Set up the game screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

# Set up the snake
SNAKE_SIZE = 10
SNAKE_COLOR = (0, 255, 0)
SNAKE_HEAD_COLOR = (0, 128, 0)
SNAKE = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
SNAKE_DIRECTION = (0, 0)

# Set up the food
FOOD_SIZE = 10
FOOD_COLOR = (255, 0, 0)
FOOD = (random.randint(0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE))

# Set up the game state
GAME_STATE = "RUNNING"

# Main game loop
while GAME_STATE == "RUNNING":
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SNAKE_DIRECTION = (0, -SNAKE_SIZE)
            elif event.key == pygame.K_DOWN:
                SNAKE_DIRECTION = (0, SNAKE_SIZE)
            elif event.key == pygame.K_LEFT:
                SNAKE_DIRECTION = (-SNAKE_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                SNAKE_DIRECTION = (SNAKE_SIZE, 0)

    # Update the snake's position
    SNAKE[0] = (SNAKE[0][0] + SNAKE_DIRECTION[0], SNAKE[0][1] + SNAKE_DIRECTION[1])

    # Check if the snake has eaten the food
    if SNAKE[0] == FOOD:
        SNAKE.append((FOOD[0], FOOD[1]))
        FOOD = (random.randint(0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE))

    # Check if the snake has hit itself or the walls
    for i in range(1, len(SNAKE)):
        if SNAKE[0] == SNAKE[i]:
            GAME_STATE = "GAME OVER"
    if SNAKE[0][0] < 0 or SNAKE[0][0] > SCREEN_WIDTH - SNAKE_SIZE or SNAKE[0][1] < 0 or SNAKE[0][1] > SCREEN_HEIGHT - SNAKE_SIZE:
        GAME_STATE = "GAME OVER"

    # Draw the game screen
    SCREEN.fill((0, 0, 0))
    for segment in SNAKE:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(SCREEN, SNAKE_HEAD_COLOR, (SNAKE[0][0], SNAKE[0][1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(SCREEN, FOOD_COLOR, (FOOD[0], FOOD[1], FOOD_SIZE, FOOD_SIZE))

    # Update the display
    pygame.display.update()

    # Clock tick
    CLOCK.tick(FPS)

# Game over
if GAME_STATE == "GAME OVER":
    print("Game over!")
    pygame.quit()
    sys.exit()
