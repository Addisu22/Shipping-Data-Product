Our Project Setup for Ethiopian Medical Business Analytics
=========================================================
Project Structure
-----------------
Shipping Data Product <br>
├── .env<br>
├── .gitignore<br>
├── README.md<br>
├── docker-compose.yml<br>
├── Dockerfile<br>
├── requirements.txt<br>
├── Data/<br>
│   ├── Raw/<br>
│   │   └── Telegram_Med_Messages/<br>
│   │       └── YYYY-MM-DD/<br>
│   │           └── channel_name.json<br>
│   └── processed/<br>
│       └── images/<br>
├── Telegram_Med_pipeline/<br>
│   ├── models/<br>
│   │   ├── staging/<br>
│   │   │   ├── stg_telegram_messages.sql<br>
│   │   │   └── ...<br>
│   │   ├── marts/<br>
│   │   │   ├── dim_channels.sql<br>
│   │   │   ├── dim_dates.sql<br>
│   │   │   └── fct_messages.sql<br>
│   │   └── ...<br>
│   ├── dbt_project.yml<br>
│   └── ...<br>
├── Script/<br>
│   ├── scraping_telegram_data.py<br>
│   ├── Telegram_data_extraction.py<br>
│   ├── Data_Enrichment.py<br>
│   └── connection.py<br>
├── api/<br>
│   ├── main.py<br>
│   ├── dbconnection.py<br>
│   ├── models.py<br>
│   ├── schemas.py<br>
│   └── cruds.py<br>
└── orchestration/<br>
    ├── __init__.py<br>
    ├── jobs.py<br>
    └── ...<br>

Task 0 - Project Setup & Environment Management
===============================================
1. Initialize Git repository
2. requirements.txt
3. Dockerfile
4. docker-compose.yml
5. .env (example)
Task 1 - Data Scraping and Collection

Task 2 - Data Modeling with DBT

Task 3 - Data Enrichment with YOLO

Task 4 - FastAPI Analytical API

Task 5 - Pipeline Orchestration with Dagster
