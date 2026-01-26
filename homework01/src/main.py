import pandas as pd

TRIPS_PATH = "/app/data/green_tripdata_2025-11.parquet"
ZONES_PATH = "/app/data/taxi_zone_lookup.csv"

def load_data():
    trips = pd.read_parquet(TRIPS_PATH)
    zones = pd.read_csv(ZONES_PATH)
    return trips, zones

def prepare_trips(trips):
    trips["lpep_pickup_datetime"] = pd.to_datetime(trips["lpep_pickup_datetime"])
    trips["pickup_date"] = trips["lpep_pickup_datetime"].dt.date
    trips["pickup_month"] = trips["lpep_pickup_datetime"].dt.month
    return trips

# Question 3
def q3(trips):
    trips_nov = trips[trips['pickup_month'] == 11]
    q3 = trips_nov[trips_nov["trip_distance"] <= 1].shape[0]
    return q3

# Question 4
def q4(trips):
    filtered = trips[trips["trip_distance"] < 100]
    daily_max = filtered.groupby("pickup_date")["trip_distance"].max() 
    q4 = daily_max.idxmax().strftime('%Y-%m-%d')
    return q4

# Question 5
def q5(trips,zones):
    target_date = pd.to_datetime('2025-11-18').date()
    day_trips = trips[trips["pickup_date"] == target_date]
    merged = day_trips.merge(zones,left_on="PULocationID",right_on="LocationID")
    grouped = merged.groupby("Zone")["total_amount"].sum()
    q5 = grouped.idxmax()
    return q5

# Question 6
# Merge with zones to get names
def q6(trips,zones):
    zone_names = zones[['LocationID', 'Zone']]

    trips_with_zones = trips.merge(zone_names,left_on='PULocationID',right_on='LocationID').rename(columns={'Zone': 'pickup_zone'}) \
    .merge(zone_names, left_on='DOLocationID', right_on='LocationID').rename(columns={'Zone': 'dropoff_zone'})

    q6 = trips_with_zones[trips_with_zones['pickup_zone'] == 'East Harlem North'] \
    .sort_values('tip_amount', ascending=False).iloc[0]['dropoff_zone']
    return q6

def main():
    trips, zones = load_data()
    trips = prepare_trips(trips)

    print("Question 3 Answer:", q3(trips))
    print("Question 4 Answer:", q4(trips))
    print("Question 5 Answer:", q5(trips, zones))
    print("Question 6 Answer:", q6(trips, zones))


if __name__ == "__main__":
    main()

