with dates as (
    select
        generate_series('2024-01-01'::date, current_date, interval '1 day') as date
),

final as (
    select
        date,
        extract(year from date) as year,
        extract(month from date) as month,
        extract(day from date) as day,
        to_char(date, 'Day') as day_name
    from dates
)

select * from final
