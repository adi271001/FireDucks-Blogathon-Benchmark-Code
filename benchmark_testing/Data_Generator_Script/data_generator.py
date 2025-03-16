import numpy as np
import pandas as pd

def generate_synthetic_data(rows=100_000_000, cols=10):
    data=np.random.rand(rows,cols)
    df=pd.DataFrame(data, columns=[f'col_{i} for i in range(cols)])
    df.to_csv("path",index=False)

if name == "main":
    generate_synthetic_data()
