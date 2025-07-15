from .jobs import etl_pipeline
from .schedules import etl_pipeline_schedule
from .sensors import new_data_sensor

from dagster import Definitions

defs = Definitions(
    jobs=[etl_pipeline],
    schedules=[etl_pipeline_schedule],
    sensors=[new_data_sensor]
)