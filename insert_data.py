import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = os.getenv("DB_PASSWORD"),
    database="bridge_db"
)

cursor = db.cursor()

base_path = "archive"   # OR full path if needed

for structure in os.listdir(base_path):
    structure_path = os.path.join(base_path, structure)

    if not os.path.isdir(structure_path):
        continue

    for condition in os.listdir(structure_path):
        condition_path = os.path.join(structure_path, condition)

        if not os.path.isdir(condition_path):
            continue

        for img in os.listdir(condition_path):
            img_path = os.path.join(condition_path, img)

            cursor.execute("""
                INSERT INTO bridge_images (image_path, structure_type, condition_type)
                VALUES (%s, %s, %s)
            """, (img_path, structure, condition))

db.commit()
print("✅ Data inserted correctly!")