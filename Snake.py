import pygame
# Initialize the pygame library
pygame.init()
# Create a screen object
screen = pygame.display.set_mode((640, 480))
# Set the background color
screen.fill((255, 255, 255))
# Create a snake object
snake = Snake()
# Start the main loop
while True:
    # Check for events
    for event in pygame.event.get():
        # If the user quits the game, exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If the user presses a key, move the snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            elif event.key == pygame.K_RIGHT:
                snake.move_right()
            elif event.key == pygame.K_UP:
                snake.move_up()
            elif event.key == pygame.K_DOWN:
                snake.move_down()
    # Update the snake's position
    snake.update()
    # Check if the snake has collided with anything
    if snake.collides_with_wall():
        # Game over
        break
    # Check if the snake has eaten any food
    if snake.eats_food():
        # Grow the snake
        snake.grow()
    # Draw the snake and the food to the screen
    snake.draw(screen)
    food.draw(screen)
    # Update the display
    pygame.display.flip()
# Quit the pygame library
pygame.quit()
