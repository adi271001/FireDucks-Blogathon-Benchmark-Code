import polars as pl
import time

df = pl.read_csv("../data/synthetic_data.csv")

start = time.time()
df_filtered = df.filter(pl.col("col_0") > 0.5)
print(f"Filter Time: {time.time() - start:.2f}s")

start = time.time()
grouped = df.groupby("col_1").agg(pl.all().mean())
print(f"GroupBy Time: {time.time() - start:.2f}s")

start = time.time()
df_sorted = df.sort("col_2")
print(f"Sort Time: {time.time() - start:.2f}s")

df2 = df.clone()
start = time.time()
df_joined = df.join(df2, on="col_3", how="inner", suffix="_right")
print(f"Join Time: {time.time() - start:.2f}s")

start = time.time()
df_rolling = df.with_columns(pl.col("col_4").rolling_mean(window_size=10).alias("rolling_mean"))
print(f"Rolling Mean Time: {time.time() - start:.2f}s")