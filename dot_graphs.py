import matplotlib.pyplot as plt

from utils import parse_file, make_dot_plot
from const import VERSIONS


finish_times = []
for name, path in VERSIONS.items():
    values, finish_time = parse_file(path)
    make_dot_plot(values, name)
    finish_times.append(finish_time)

# Assuming colors is a list of your column colors
colors = ['r', 'g', 'b']

bars = plt.bar(range(len(finish_times)), finish_times, alpha=0.5, color=colors, tick_label=VERSIONS.keys())

# Set the title and labels
plt.title('Гистограмы времени обучения одной эпохи')
plt.ylabel('Время обучения сек.')

# Add the finish times as text on the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

# Show the plot
plt.show()

# cluster
values, finish_time = parse_file('outputs/cluster_mkl.txt')
indices = list(range(len(values)))
mean_time = sum(values) / len(values)

plt.figure(figsize=(10, 5))
plt.plot(indices, values, marker='o', linestyle='None', color='b', markersize=4)

plt.title('cluster MKL')  # Название графика
plt.xlabel('Индекс батча')  # Подпись оси X
plt.ylabel('Время обучения с.')  # Подпись оси Y
plt.grid(True)

# plt.ylim(4, 36)
plt.axhline(y=mean_time, color='r', linestyle='--', label=f'Среднее значение: {mean_time:.2f} сек.')

plt.legend()
plt.show()
