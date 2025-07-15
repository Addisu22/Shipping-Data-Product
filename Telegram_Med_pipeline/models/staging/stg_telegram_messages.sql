with source as (
    select * from raw.raw_telegram_messages
),

renamed as (
    select
        message_id,
        sender_id,
        date::timestamp as message_date,
        text,
        channel,
        media_type,
        length(text) as message_length,
        case when media_type = 'MessageMediaPhoto' then true else false end as has_image
    from source
)

select * from renamed
