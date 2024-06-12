import matplotlib.pyplot as plt


def parse_file(file_path: str) -> (list[float], float):
    file = open(file_path, 'r')
    lines = file.read().split('\n')
    values = [float(line[line.find(':') + 3:]) for line in lines if 'time:' in line]
    finish_time = values.pop()
    return values, finish_time


def make_dot_plot(values: list[float], torch_version: str):
    indices = list(range(len(values)))
    mean_time = sum(values) / len(values)

    plt.figure(figsize=(10, 5))
    plt.plot(indices, values, marker='o', linestyle='None', color='b', markersize=4)

    plt.title(torch_version)  # Название графика
    plt.xlabel('Индекс батча')  # Подпись оси X
    plt.ylabel('Время обучения с.')  # Подпись оси Y
    plt.grid(True)

    plt.ylim(4, 36)
    plt.axhline(y=mean_time, color='r', linestyle='--', label=f'Среднее значение: {mean_time:.2f} сек.')

    plt.legend()
    plt.show()
