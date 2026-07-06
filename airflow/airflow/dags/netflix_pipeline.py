from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Shariq",
}

with DAG(
    dag_id="netflix_data_pipeline",
    default_args=default_args,
    description="Netflix Data Engineering Pipeline using Spark",
    start_date=datetime(2026, 7, 6),
    schedule=None,
    catchup=False,
    tags=["Netflix", "Spark"],
) as dag:

    ingestion = BashOperator(
        task_id="data_ingestion",
        bash_command="""
        cd /opt/project
        python -m Spark.scripts.01_data_ingestion
        """,
    )

    transformation = BashOperator(
        task_id="data_transformation",
        bash_command="""
        cd /opt/project
        python -m Spark.scripts.02_data_transformation
        """,
    )

    analysis = BashOperator(
        task_id="data_analysis",
        bash_command="""
        cd /opt/project
        python -m Spark.scripts.03_data_analysis
        """,
    )

    ingestion >> transformation >> analysis