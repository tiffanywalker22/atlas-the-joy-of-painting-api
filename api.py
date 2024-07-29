from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

db_config = {
    'dbname': 'joy_of_painting',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn

@app.route('/episodes', methods=['GET'])
def get_episodes():
    month = request.args.get('month')
    subjects = request.args.getlist('subject')
    colors = request.args.getlist('color')
    filter_type = request.args.get('filter_type', 'AND').upper()

    conn = connect_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    query = "SELECT * FROM episodes WHERE TRUE"
    params = []

    if month:
        query += " AND month = %s"
        params.append(month)

    if subjects:
        if filter_type == 'AND':
            for subject in subjects:
                query += " AND %s = ANY (string_to_array(subject, ', '))"
                params.append(subject)
        else:
            query += " AND (" + " OR ".join(["%s = ANY (string_to_array(subject, ', '))"] * len(subjects)) + ")"
            params.extend(subjects)

    if colors:
        if filter_type == 'AND':
            for color in colors:
                query += " AND %s = ANY (string_to_array(colors, ', '))"
                params.append(color)
        else:
            query += " AND (" + " OR ".join(["%s = ANY (string_to_array(colors, ', '))"] * len(colors)) + ")"
            params.extend(colors)

    cursor.execute(query, params)
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()

    episodes_list = [dict(episode) for episode in episodes]
    return jsonify(episodes_list)

if __name__ == '__main__':
    app.run(debug=True)
