
    

    create  table
      "analytics"."main"."fct_customer_orders__dbt_tmp"
  
    
    as (
      ﻿with customers as (
    select * from "analytics"."main"."stg_customers"
),
orders as (
    select * from "analytics"."main"."stg_orders"
)
select
    c.customer_id,
    c.customer_name,
    c.customer_region,
    count(case when o.order_status = 'completed' then o.order_id end) as total_completed_orders,
    coalesce(sum(case when o.order_status = 'completed' then o.order_amount else 0 end), 0) as total_spend_usd,
    min(o.order_date) as first_order_date,
    max(o.order_date) as latest_order_date
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name, c.customer_region
    );
    
  