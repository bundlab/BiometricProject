import cv2
import numpy as np
from utils.helpers import get_db_connection

def capture_fingerprint():
    # Simulate fingerprint scanning (Replace with actual fingerprint scanner SDK)
    print("Scanning fingerprint...")
    img = cv2.imread("fingerprint_sample.jpg", 0)  # Load fingerprint image
    return np.array(img).tobytes()  # Convert to byte array

def save_fingerprint(user_id, fingerprint_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, fingerprint) VALUES (%s, %s)",
        (user_id, fingerprint_data)
    )
    conn.commit()
    cursor.close()
    conn.close()
