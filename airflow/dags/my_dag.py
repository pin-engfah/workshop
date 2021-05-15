# my_dag.py

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone

def _create_homepage():
    with open("html/index.html", "w") as f:
        f.writelines("<h1>Welcome to My Course</h1>")
        f.writelines("<p>It's raining day.. :'(</p>")

default_args = {
    "owner": "fahpin",
    "start_date": timezone.datetime(2021, 5, 15),
}
with DAG("my_dag", 
         schedule_interval="*/5 * * * *",
         default_args=default_args,
         catchup=False) as dag:

    start = DummyOperator(task_id="start")

    create_homapage = PythonOperator(
        task_id = "create_homapage",
        python_callable = _create_homepage,
    )

    end = DummyOperator(task_id="end")

    start >> create_homapage >> end