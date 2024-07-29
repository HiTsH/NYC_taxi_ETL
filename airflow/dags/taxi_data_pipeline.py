# Imports
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'taxi_data_pipeline',
    default_args=default_args,
    description='An end-to-end data pipeline for NYC taxi data',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(task_id='start', dag=dag)

def run_spark_job():
    subprocess.run(['spark-submit', '--master', 'spark://spark-master:7077', '/opt/spark/jobs/spark_job.py'])

spark_task = PythonOperator(
    task_id='run_spark_job',
    python_callable=run_spark_job,
    dag=dag,
)

start >> spark_task
