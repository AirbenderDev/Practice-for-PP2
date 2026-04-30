import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def init_db():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            );
        ''')
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print("DB error:", e)
        return False


def get_player_id(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO players(username) VALUES(%s) ON CONFLICT(username) DO NOTHING", (username,))
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    player_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return player_id


def save_result(username, score, level):
    try:
        player_id = get_player_id(username)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO game_sessions(player_id, score, level_reached) VALUES(%s, %s, %s)",
            (player_id, score, level)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Save result error:", e)


def get_personal_best(username):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT COALESCE(MAX(gs.score), 0)
            FROM game_sessions gs
            JOIN players p ON p.id = gs.player_id
            WHERE p.username = %s
        ''', (username,))
        best = cur.fetchone()[0]
        cur.close()
        conn.close()
        return best
    except Exception:
        return 0


def get_top10():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT p.username, gs.score, gs.level_reached, TO_CHAR(gs.played_at, 'YYYY-MM-DD HH24:MI')
            FROM game_sessions gs
            JOIN players p ON p.id = gs.player_id
            ORDER BY gs.score DESC, gs.level_reached DESC
            LIMIT 10
        ''')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception:
        return []
