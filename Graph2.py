import graphics as g

# Create the canvas, 20x20 pixels (characters).
screen = g.Canvas(size = (20, 20))

# Create a circle image, radius 5 pixels.
circleImage = g.shapes.Circle(5)

# Create a green sprite at position (7, 7) with the circle image.
circleSprite = g.Sprite(circleImage,
                        position = (7, 7),
                        color = g.colors.GREEN)

# Add the sprite to the canvas.
screen.sprites.append(circleSprite)

# Output the canvas to the terminal.
print(screen)

# Increase the circles radius by two.
circleSprite.image.radius += 2

# Output the canvas to the terminal.
print(screen)