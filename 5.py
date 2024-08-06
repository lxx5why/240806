import matplotlib.pyplot as plt

x = [65, 70, 70, 75, 80, 85, 85, 80]
y = [17, 18, 19, 20, 21, 22, 23, 24]

plt.plot(x, y, marker = '*', linestyle = '-', color = 'red', label = "humidity")
plt.title("Daily humidity trend")
plt.xlabel("Humidity (H)")
plt.ylabel("Time (Hour)")
plt.legend()
plt.grid(True)
plt.show()