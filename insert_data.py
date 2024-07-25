import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='new_user',
        password='securepassword',
        database='joy_of_painting'
    )

def insert_episode(title, date, month, episode, painting_index, img_src, youtube_src, num_colors, colors, subject, color_hex):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO episodes (title, date, month, episode, painting_index, img_src, youtube_src, num_colors, colors, subject, color_hex)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (title, date, month, episode, painting_index, img_src, youtube_src, num_colors, colors, subject, color_hex))
    conn.commit()
    cursor.close()
    conn.close()
