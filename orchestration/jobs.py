from dagster import job, op, get_dagster_logger
import os
from dotenv import load_dotenv

load_dotenv()

logger = get_dagster_logger()

@op
def scrape_telegram_data(context):
    from scripts.scrape_telegram import main
    import asyncio
    asyncio.run(main())
    return True

@op
def load_raw_to_postgres(context, success):
    if not success:
        raise Exception("Scraping failed, skipping load")
    
    from scripts.load_raw_data import main
    main()
    return True

@op
def run_dbt_transformations(context, success):
    if not success:
        raise Exception("Loading failed, skipping dbt")
    
    os.system("cd dbt && dbt run")
    return True

@op
def run_yolo_enrichment(context, success):
    if not success:
        raise Exception("DBT failed, skipping YOLO")
    
    from scripts.image_processing import process_images
    process_images()
    return True

@job
def etl_pipeline():
    scrape_success = scrape_telegram_data()
    load_success = load_raw_to_postgres(scrape_success)
    dbt_success = run_dbt_transformations(load_success)
    run_yolo_enrichment(dbt_success)