import matplotlib.pyplot as plt
import numpy as np

from utils import parse_file
from const import VERSIONS


# Указываем границы интервалов (бинов)
bins = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

for name, path in VERSIONS.items():
    values, _ = parse_file(path)
    mean_value = np.mean(values)

    plt.hist(values, bins=bins, edgecolor='black')
    plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Мат. ожидание: {mean_value:.2f}')
    # plt.text(mean_value, plt.ylim()[1] * 0.95, f'Математическое ожидание: {mean_value:.2f}',
    #          color='red', ha='center')

    plt.xlabel('Временные интервалы')
    plt.ylabel('Количество временных значений')
    plt.title(name)
    plt.ylim(0, 600)

    plt.legend()
    plt.show()

