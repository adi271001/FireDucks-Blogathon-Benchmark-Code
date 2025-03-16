import fireducks as fd
import time

df = fd.read_csv("../data/synthetic_data.csv")

start = time.time()
df_filtered = df[df['col_0'] > 0.5]
print(f"Filter Time: {time.time() - start:.2f}s")

start = time.time()
grouped = df.groupby('col_1').mean()
print(f"GroupBy Time: {time.time() - start:.2f}s")

start = time.time()
df_sorted = df.sort_values('col_2')
print(f"Sort Time: {time.time() - start:.2f}s")

df2 = df.copy()
start = time.time()
df_joined = df.merge(df2, on='col_3', suffixes=('_left', '_right'))
print(f"Join Time: {time.time() - start:.2f}s")

start = time.time()
df['rolling_mean'] = df['col_4'].rolling(window=10).mean()
print(f"Rolling Mean Time: {time.time() - start:.2f}s")