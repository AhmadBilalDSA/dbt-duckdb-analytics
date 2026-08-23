
  
  create view "analytics"."main"."stg_customers__dbt_tmp" as (
    ﻿with source as (
    select * from "analytics"."main"."raw_customers"
)
select
    cast(customer_id as integer) as customer_id,
    trim(name) as customer_name,
    cast(signup_date as date) as signup_date,
    trim(region) as customer_region
from source
  );
