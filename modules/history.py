import sqlite3
import os
from datetime import datetime, timedelta

def extract_history(db_path):
    if not os.path.exists(db_path):
        return ["Error: File does not exist."]

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT url, title, last_visit_time 
            FROM urls 
            ORDER BY last_visit_time DESC 
            LIMIT 20
        """)
        results = cursor.fetchall()
        output = []

        for url, title, visit_time in results:
            readable_time = chrome_time_to_datetime(visit_time)
            output.append(f"{readable_time} | {title or '(No Title)'} | {url}")

        conn.close()
        return output

    except Exception as e:
        return [f"Error reading history: {e}"]

def chrome_time_to_datetime(chrome_time):
    try:
        # Chrome stores timestamps as microseconds since 1601
        return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Invalid Time"


