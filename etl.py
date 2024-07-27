import csv
import psycopg2

db_config = {
    'dbname': 'joy_of_painting',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

def connect_db(config):
    conn = psycopg2.connect(**config)
    return conn

def insert_episode(cursor, episode):
    insert_query = """
    INSERT INTO episodes (title, date, month, episode, painting_index, img_src, youtube_src, num_colors, colors, subject, color_hex)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, episode)

def process_csv(file_path, db_config):
    conn = connect_db(db_config)
    cursor = conn.cursor()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            episode = (
                row['Title'],
                row['Date'],
                row['Month'],
                row['Episode'],
                int(row['painting_index']),
                row['img_src'],
                row['youtube_src'],
                int(row['num_colors']),
                row['colors'],
                row['subject'],
                row['color_hex']
            )
            insert_episode(cursor, episode)
    conn.commit()
    cursor.close()
    conn.close()

csv_file_path = 'new_dataset.csv'

process_csv(csv_file_path, db_config)