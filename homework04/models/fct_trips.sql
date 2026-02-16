select
    *,
    extract(year from pickup_datetime) as year,
    extract(month from pickup_datetime) as month
from {{ ref('int_trips_unioned') }}
