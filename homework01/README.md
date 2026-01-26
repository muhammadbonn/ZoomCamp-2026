# ZoomCamp 2026 – Homework 01 (Green Taxi Analysis)

This project contains the solution for Homework 01 of the Data Engineering ZoomCamp 2026.
The analysis is performed using Python (pandas) inside a Docker + Docker Compose environment to ensure reproducibility.

Overview:
The homework analyzes the Green Taxi trips dataset for November 2025 by reading Parquet data,
applying filters and aggregations with pandas, and running everything inside a Docker container.

Project Structure:
homework01/green_taxi
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── src/
│   └── main.py
└── data/
    ├── green_tripdata_2025-11.parquet
    └── taxi_zone_lookup.csv

Clone the Repository:
git clone https://github.com/muhammadbonn/ZoomCamp-2026.git
cd ZoomCamp-2026/homework01/green_taxi

Build the Docker Image:
docker compose build --no-cache

Run the Analysis:
docker compose run --rm app

Or run interactively:
docker compose up
docker compose exec app bash
python src/main.py

Reference:
https://github.com/DataTalksClub/data-engineering-zoomcamp
