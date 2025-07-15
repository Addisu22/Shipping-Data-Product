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
def ensure_detection_table(cursor, conn):
    cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS analytics;

        CREATE TABLE IF NOT EXISTS analytics.fct_image_detections (
            detection_id SERIAL PRIMARY KEY,
            message_id INT,
            detected_object_class TEXT,
            confidence_score FLOAT,
            image_path TEXT
        );
    """)
    conn.commit()

# Detect and insert
def detect_objects_in_images(image_dir, mapping_json):
    model = YOLO("yolov8n.pt")  # or yolov8s.pt, yolov8m.pt

    # Load image-message_id mapping
    with open(mapping_json, 'r', encoding='utf-8') as f:
        image_map = json.load(f)

    conn = getpgsql_connect()
    cursor = conn.cursor()
    ensure_detection_table(cursor, conn)

    insert_data = []

    for image_file, message_id in image_map.items():
        image_path = os.path.join(image_dir, image_file)

        if not os.path.exists(image_path):
            continue

        results = model(image_path)
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[cls_id]

                insert_data.append((
                    message_id,
                    class_name,
                    confidence,
                    image_path
                ))

    if insert_data:
        execute_values(cursor, """
            INSERT INTO analytics.fct_image_detections
            (message_id, detected_object_class, confidence_score, image_path)
            VALUES %s
        """, insert_data)
        conn.commit()
        print(f" Inserted {len(insert_data)} detections")

    cursor.close()
    conn.close()