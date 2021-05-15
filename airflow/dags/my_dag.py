# my_dag.py

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils import timezone


default_args = {
    "owner": "zkan",
    "start_date": timezone.datetime(2021, 5, 15),
}
with DAG("my_dag", 
         schedule_interval="@daily",
         default_args=default_args,
         catchup=False) as dag:

    start = DummyOperator(task_id="start")

    end = DummyOperator(task_id="end")

    start >> end