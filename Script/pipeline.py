from dagster import op, job
import subprocess

@op
def scrape_telegram_data():
    # Run your telegram scraping script, e.g. scrape.py
    subprocess.run(["python", "scrape.py"], check=True)

@op
def load_raw_to_postgres():
    # Run your data loading script
    subprocess.run(["python", "load_raw_to_postgres.py"], check=True)

@op
def run_dbt_transformations():
    # Run dbt commands, assuming dbt project is in current directory
    subprocess.run(["dbt", "run"], check=True)
    subprocess.run(["dbt", "test"], check=True)

@op
def run_yolo_enrichment():
    # Run your YOLO object detection enrichment script
    subprocess.run(["python", "detect_objects.py"], check=True)
