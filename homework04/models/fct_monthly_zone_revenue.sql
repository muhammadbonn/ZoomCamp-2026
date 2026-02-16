select
    year,
    month,
    pickup_location_id as zone_id,
    sum(total_amount) as revenue,
    count(*) as total_trips
from {{ ref('fct_trips') }}
group by year, month, pickup_location_id
