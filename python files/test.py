import matplotlib.pyplot as plt

money = 0

y = []
x = []

for i in range(6):
    money += 700
    money = money * 1.08
    y.append(money / 100)
    x.append(i)

print(money)
plt.plot(x, y)
plt.title("Money Over Time")
plt.savefig("test_plot.png")  # Save the plot as a file
plt.show()  # Show the plot
