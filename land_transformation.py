import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Matrix creation
A = np.random.randint(1, 16, size=(15, 15))

# color assignment function
def color_assignment(number):
    if number <= 10:
        return 'green'
    if 10 < number < 13:
        return "grey"
    else:
        return 'blue'

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Color matrix creation
matrix_color = np.vectorize(color_assignment)(A)

# Counter to keep track of the number of iterations
iteration_count = 0

# Function to update the plot for each animation frame
def update(frame):
    global A, iteration_count
    ax.clear()
    
    # Add random values from -2 to +2 to each cell
    A += np.random.randint(-2, 3, size=A.shape)

    # Color matrix creation
    matrix_color = np.vectorize(color_assignment)(A)

    # Display the color matrix as squares
    ax.imshow(np.zeros_like(A), cmap='Greys', interpolation='none')
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            ax.fill_between([j, j+1], i, i+1, color=matrix_color[i, j])

    ax.set_xticks([])
    ax.set_yticks([])

    # Increment the iteration count
    iteration_count += 1

    # Display the current iteration count as a label
    ax.text(0.5, -0.1, f'Iteration {iteration_count}', transform=ax.transAxes, fontsize=12, ha='center')


    # Stop the animation after 10 iterations
    if iteration_count >= 500:
        ani.event_source.stop()

    

# Create an animation that updates every 2 seconds
ani = FuncAnimation(fig, update, interval=100)

# Show the animation
plt.show()