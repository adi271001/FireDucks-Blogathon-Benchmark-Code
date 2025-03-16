# AI & Data Science Blogathon - Benchmarking DataFrame Libraries

This repo contains benchmark analysis and visualizations comparing Pandas, FireDucks, Polars, and Modin on ETL tasks.

# FireDucks Benchmark Blog: Pandas vs. FireDucks vs. Polars vs. Modin

## 📖 Overview
This repository contains all the resources, code, and benchmarking results for the blog:
**"Pandas vs. FireDucks vs. Polars vs. Modin: Which One Wins?"**

It evaluates four major DataFrame engines in Python for real-world ETL workloads on large-scale data (100M+ rows). The project is a part of the **AI & Data Science Blogathon** hosted by FireDucks and devrelsquad.live.

## 📈 Benchmark Scope
- Dataset Size: 100 million rows x 10 numerical columns
- Tasks:
  - CSV Loading
  - Row Filtering
  - GroupBy Aggregation
  - Sorting
  - Join Operations
  - Rolling Window Computation

## 🧠 Tools Compared
- **Pandas** — Classic, in-memory single-threaded
- **FireDucks** — High-performance, multithreaded, out-of-core
- **Polars** — Rust-based, lazy execution with Arrow
- **Modin** — Pandas-compatible distributed engine (Ray/Dask)

## 🖥️ Environment
- CPU: 16-core Intel Xeon
- RAM: 32 GB DDR4
- OS: Ubuntu 22.04 LTS

## 📂 Directory Structure
```
benchmarks_testing
├── benchmark_scripts/
│   ├── pandas_benchmark.py
│   ├── fireducks_benchmark.py
│   ├── polars_benchmark.py
│   └── modin_benchmark.py
├── data_generator/
│   └── synthetic_data_generator.py
├── data/
    └── path.csv/data.md
├── research_papers/
├── plots/
│   └── benchmark_chart.png
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/<your-username>/fireducks-benchmark-blog.git
cd fireducks-benchmark-blog
```
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Run Benchmarks
```bash
python benchmark_scripts/fireducks_benchmark.py
python benchmark_scripts/polars_benchmark.py
python benchmark_scripts/pandas_benchmark.py
python benchmark_scripts/modin_benchmark.py
```


## Signature
Aditya D
* Github: https://wwww.github.com/adi271001
* LInkedin: https://www.linkedin.com/in/aditya-d-23453a179/
* Topmate: https://topmate.io/aditya_d/
* Twitter: https://x.com/ADITYAD29257528

## License
Apache 2.0
