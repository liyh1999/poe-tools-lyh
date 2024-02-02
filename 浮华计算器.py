import numpy as np
import matplotlib.pyplot as plt
def plot_function_floor_values_with_change_points_and_values(x):
    y_values = np.linspace(1, 1.5, 500)  # More points for better precision
    function_values = x * (1 + y_values)
    floor_function_values = np.floor(function_values)

    # Find the points where the floored value changes
    change_indices = np.where(np.diff(floor_function_values) != 0)[0]
    change_points = y_values[change_indices + 1]
    change_values = floor_function_values[change_indices + 1]

    # Plotting
    plt.plot(y_values, floor_function_values, label='Floored Value')
    plt.scatter(change_points, change_values, color='red', label='Change Points')  # Mark change points
    for cp, cv in zip(change_points, change_values):
        plt.text(cp, cv, f'({cp:.2f}, {int(cv)})', fontsize=8, verticalalignment='bottom')  # Annotate the change points

    plt.xlabel('y')
    plt.ylabel('Floored value of x*(1+y)')
    plt.title(f'Plot of Floored value of x*(1+y) with Change Points for x={x}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example with x=10
plot_function_floor_values_with_change_points_and_values(8)


