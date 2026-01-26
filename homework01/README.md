# Data Engineering ZoomCamp 2026 – Homework 01 (Green Taxi Analysis)

This repository contains the solution for **Homework 01** of the [Data Engineering ZoomCamp 2026]. The project analyzes Green Taxi trip data from **November 2025** using Python (pandas) within a Dockerized environment to ensure full reproducibility.

---

## Overview
The analysis involves reading Parquet data, performing complex merges with taxi zone lookups, and calculating trip statistics (such as identifying high-tip destinations). All processes are encapsulated within a Docker container.

---

## Project Structure
```text
homework01/green_taxi/
├── src/
│   └── main.py             # Analysis script (Pandas logic)
├── data/
│   ├── green_tripdata_2025-11.parquet
│   └── taxi_zone_lookup.csv
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Orchestration for the app
├── requirements.txt        # Python library dependencies
└── README.md               # Documentation
```

### Getting Started
1. Clone the Repository
```
git clone https://github.com
cd ZoomCamp-2026/homework01/green_taxi
```
2. Build the Docker Image
```
docker compose build --no-cache
```
3. Run the Analysis
```
docker compose run --rm app
```
Or run interactively (Bash):
```
docker compose up -d
docker compose exec app bash
python src/main.py
```



