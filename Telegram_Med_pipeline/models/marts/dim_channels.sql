with base as (
    select distinct channel
    from {{ ref('stg_telegram_messages') }}
),

final as (
    select
        channel,
        md5(channel) as channel_id
    from base
)

select * from final
