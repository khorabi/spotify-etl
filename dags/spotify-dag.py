from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

from spotify_etl import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past' : False,
    'start_date': datetime(2021, 7, 27), #data do dia de início
    'email': ['example@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}



dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='Our first dag with ETL process',
    schedule_interval=timedelta(minutes=60)
)


run_etl = PythonOperator(
    task_id='whole_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag
)

run_etl