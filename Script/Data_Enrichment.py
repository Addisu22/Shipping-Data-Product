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
def ensure_enriched_table(cursor, conn):
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
    conn.commit()

def detect_objects_in_images(image_dir, mapping_json_path):
    print(f"Loading YOLOv8 model...")
    model = YOLO("yolov8n.pt")  # lightweight model

    print(f"Loading image-message mapping from {mapping_json_path}...")
    with open(mapping_json_path, 'r', encoding='utf-8') as f:
        image_map = json.load(f)  # {image_filename: message_id}

    conn = getpgsql_connect()
    cursor = conn.cursor()

    ensure_enriched_table(cursor, conn)

    detections = []
    total_images = len(image_map)
    processed_images = 0
    skipped_images = 0

    for image_file, message_id in image_map.items():
        image_path = os.path.join(image_dir, image_file)
        if not os.path.exists(image_path):
            print(f"Image not found, skipping: {image_path}")
            skipped_images += 1
            continue

        print(f"Processing image: {image_path}")
        results = model(image_path)

        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls)]
                conf = float(box.conf)
                detections.append((message_id, image_file, cls, conf))
                print(f" - Detected {cls} with confidence {conf:.2f}")

        processed_images += 1

    if detections:
        insert_query = """
            INSERT INTO enriched.fct_image_detections 
            (message_id, image_file, detected_class, confidence_score)
            VALUES %s
        """
        execute_values(cursor, insert_query, detections)
        conn.commit()
        print(f"\n Inserted {len(detections)} detections into the database.")
    else:
        print("\nℹ No detections to insert.")

    cursor.close()
    conn.close()

    print(f"\nSummary:")
    print(f" - Total images in mapping: {total_images}")
    print(f" - Images processed: {processed_images}")
    print(f" - Images skipped (missing files): {skipped_images}")
    print(f" - Total detections found: {len(detections)}")

    return detections