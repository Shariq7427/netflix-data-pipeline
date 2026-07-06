from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def health_check():
    print("Netflix Pipeline Running")

with DAG(
    dag_id='netflix_pipeline',
    start_date=datetime(2025,1,1),
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='health_check',
        python_callable=health_check
    )