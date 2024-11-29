import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 50]

plt.plot(y, x)
plt.title("Test Plot")
plt.savefig("test_plot.png")  # Save the plot as a file
plt.show()  # Show the plot
