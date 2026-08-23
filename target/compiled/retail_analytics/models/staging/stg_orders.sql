with source as (
    select * from "analytics"."main"."raw_orders"
)
select
    cast(order_id as integer) as order_id,
    cast(customer_id as integer) as customer_id,
    cast(order_date as date) as order_date,
    trim(status) as order_status,
    cast(amount as decimal(10, 2)) as order_amount
from source