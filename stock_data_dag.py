from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Update the path to your script
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from stock_data import main

default_args = {
    "owner": "your_name",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "stock_data_dag",
    default_args=default_args,
    schedule_interval=timedelta(hours=1),  # Adjust the interval as needed
    catchup=False,
) as dag:

    run_stock_data_script = PythonOperator(
        task_id="run_stock_data_script",
        python_callable=main,
    )

    run_stock_data_script
