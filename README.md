Our Project Setup for Ethiopian Medical Business Analytics
=========================================================
Project Structure
-----------------
Shipping Data Product
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── Data/
│   ├── Raw/
│   │   └── Telegram_Med_Messages/
│   │       └── YYYY-MM-DD/
│   │           └── channel_name.json
│   └── processed/
│       └── images/
├── Telegram_Med_pipeline/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_telegram_messages.sql
│   │   │   └── ...
│   │   ├── marts/
│   │   │   ├── dim_channels.sql
│   │   │   ├── dim_dates.sql
│   │   │   └── fct_messages.sql
│   │   └── ...
│   ├── dbt_project.yml
│   └── ...
├── Script/
│   ├── scraping_telegram_data.py
│   ├── Telegram_data_extraction.py
│   ├── Data_Enrichment.py
│   └── connection.py
├── api/
│   ├── main.py
│   ├── dbconnection.py
│   ├── models.py
│   ├── schemas.py
│   └── cruds.py
└── orchestration/
    ├── __init__.py
    ├── jobs.py
    └── ...