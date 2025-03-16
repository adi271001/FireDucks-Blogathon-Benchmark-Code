import matplotlib.pyplot as plt
import numpy as np

# Benchmark data
labels = ['Load', 'Filter', 'GroupBy', 'Sort', 'Join', 'Rolling']
pandas = [25, 4.5, 6.2, 5.8, 7.1, 6.0]
fireducks = [7, 1.2, 1.8, 2.3, 2.7, 2.0]
polars = [9, 1.4, 2.1, 2.5, 3.0, 2.6]
modin = [20, 3.0, 3.9, 4.7, 5.2, 4.8]

x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - 1.5*width, pandas, width, label='Pandas')
ax.bar(x - 0.5*width, fireducks, width, label='FireDucks')
ax.bar(x + 0.5*width, polars, width, label='Polars')
ax.bar(x + 1.5*width, modin, width, label='Modin')

ax.set_ylabel('Execution Time (seconds)')
ax.set_title('ETL Benchmark: DataFrame Libraries Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/benchmark_chart.png")
plt.show()
