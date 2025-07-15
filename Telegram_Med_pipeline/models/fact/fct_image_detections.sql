with detections as (
    select
        id as detection_id,
        message_id,
        image_file,
        detected_object_class,
        confidence_score,
        detected_at
    from {{ source('enriched', 'fct_image_detections') }}
),

messages as (
    select
        id as message_id,
        channel_id,
        date,
        text,
        -- other relevant fields
    from {{ ref('fct_messages') }}
),

channels as (
    select
        id as channel_id,
        channel_name,
        -- other channel dimension fields
    from {{ ref('dim_channels') }}
)

select
    d.detection_id,
    d.message_id,
    d.image_file,
    d.detected_object_class,
    d.confidence_score,
    d.detected_at,
    m.channel_id,
    m.date,
    m.text,
    c.channel_name

from detections d
left join messages m on d.message_id = m.message_id
left join channels c on m.channel_id = c.channel_id