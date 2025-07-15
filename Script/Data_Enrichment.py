from ultralytics import YOLO
import os
import json
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
from datetime import datetime
from PIL import Image
from connection import *
# Load environment variables
load_dotenv()

# PostgreSQL connection
conn = getpgsql_connect()

# Ensure YOLO detections table
def ensure_detection_table(cursor):
    cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS enriched;
        CREATE TABLE IF NOT EXISTS enriched.fct_image_detections (
            id SERIAL PRIMARY KEY,
            message_id INT,
            image_file TEXT,
            detected_class TEXT,
            confidence_score FLOAT,
            detected_at TIMESTAMP DEFAULT NOW()
        );
    """)

def detect_objects_in_images(image_dir, mapping_json):
    model = YOLO("yolov8n.pt")  # lightweight YOLOv8 model
    detections = []

    with open(mapping_json, 'r', encoding='utf-8') as f:
        image_map = json.load(f)

    conn = getpgsql_connect()
    cursor = conn.cursor()
    ensure_detection_table(cursor)

    for image_file, message_id in image_map.items():
        image_path = os.path.join(image_dir, image_file)

        if not os.path.exists(image_path):
            print(f" Image not found: {image_path}")
            continue

        results = model(image_path)
        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls)]
                conf = float(box.conf)
                detections.append((message_id, image_file, cls, conf))

    # Insert into DB
    insert_query = """
        INSERT INTO enriched.fct_image_detections 
        (message_id, image_file, detected_class, confidence_score)
        VALUES %s
    """
    execute_values(cursor, insert_query, detections)
    conn.commit()
    cursor.close()
    conn.close()

    print(f" Detected and saved {len(detections)} records.")
    return detections