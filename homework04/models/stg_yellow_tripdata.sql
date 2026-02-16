with raw as (
    select *
    from prod.yellow_tripdata
)

select
    vendorid,
    tpep_pickup_datetime  as pickup_datetime,
    tpep_dropoff_datetime as dropoff_datetime,
    passenger_count,
    trip_distance,
    ratecodeid,
    store_and_fwd_flag,
    payment_type,
    NULL as trip_type,   -- Added to match Green taxi
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    PULocationID   as pickup_location_id,
    DOLocationID   as dropoff_location_id
from raw
