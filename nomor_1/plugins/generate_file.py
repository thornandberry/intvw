import sqlite3
import pandas as pd

def generate_file():

    dag_dir = "/opt/airflow"

    conn = sqlite3.connect(f'{dag_dir}/data/dwh.db')
    print("Connect db success")

    query1 = "SELECT * FROM dim_customer"
    query2 = "SELECT * FROM dim_date"
    query3 = "SELECT * FROM fact_order_accumulating"

    df1 = pd.read_sql(query1, conn)
    df2 = pd.read_sql(query2, conn)
    df3 = pd.read_sql(query3, conn)

    df1.to_excel(f'{dag_dir}/data/dim_customer.xlsx')
    df2.to_excel(f'{dag_dir}/data/dim_date.xlsx')
    df3.to_excel(f'{dag_dir}/data/fact_order_accumulating.xlsx')

if __name__ == '__main__':

    generate_file()