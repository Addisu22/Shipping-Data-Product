with messages as (
    select * from {{ ref('stg_telegram_messages') }}
),

channels as (
    select * from {{ ref('dim_channels') }}
),

dates as (
    select * from {{ ref('dim_dates') }}
),

final as (
    select
        m.message_id,
        c.channel_id,
        d.date,
        m.message_length,
        m.has_image
    from messages m
    join channels c on m.channel = c.channel
    join dates d on m.message_date::date = d.date
)

select * from final
