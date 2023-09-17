
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib basics
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Matplotlib Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Seaborn for advanced visualizations
sns.set_theme()
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", size="size", data=tips)
plt.title("Seaborn Example: Tips Dataset")
plt.show()
