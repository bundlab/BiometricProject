import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="biometric_db",
        user="postgres",
        password="Mypg@25",
        host="localhost",
        port="5432"
    )

def insert_user(name, fingerprint_data, face_encoding):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, fingerprint, face_encoding) VALUES (%s, %s, %s)",
        (name, fingerprint_data, face_encoding)
    )
    conn.commit()
    cursor.close()
    conn.close()