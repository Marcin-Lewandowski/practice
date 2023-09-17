from random import randint
import numpy as np
import matplotlib.pyplot as plt

# Matrix creation
A = np.random.randint(1, 16, size=(50, 50))


# color assignment function
def color_assignment(number):
    if number <= 10:
        return 'green'
    if number > 10 and number < 13:
        return "grey"
    else:
        return 'blue'

# Color matrix creation
matrix_color = np.vectorize(color_assignment)(A)


# Display the color matrix as squares
plt.imshow(np.zeros_like(A), cmap='Greys', interpolation='none')
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        plt.fill_between([j, j+1], i, i+1, color=matrix_color[i, j])
plt.xticks([])
plt.yticks([])
plt.show()