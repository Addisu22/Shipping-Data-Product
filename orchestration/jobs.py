@job
def telegram_data_pipeline():
    scrape = scrape_telegram_data()
    load = load_raw_to_postgres()
    dbt = run_dbt_transformations()
    yolo = run_yolo_enrichment()

    # Define dependencies (linear for example)
    load.wait_for(scrape)
    dbt.wait_for(load)
    yolo.wait_for(dbt)