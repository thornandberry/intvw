import sqlite3
import sys

def run_sql():

    dag_dir = "/opt/airflow"

    query = open(f'{dag_dir}/queries/{filename}').read()
    print("Reading query success")

    conn = sqlite3.connect(f'{dag_dir}/data/dwh.db')
    print("Connect db success")

    cur = conn.cursor()
    cur.executescript(query)
    conn.close()
    print("Query executed successfully")

if __name__ == '__main__':
    filename = sys.argv[1]

    run_sql()