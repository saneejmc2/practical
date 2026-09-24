#Import essential libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

# Define DAG
@dag(
    dag_id='action_operator_bash',
    description='A simple DAG to demonstrate operator action',
    start_date=datetime(2026, 9, 13),
    catchup=False,
    tags=['bash_operator'],
)
def my_task():
    List_dag_files = BashOperator(
        task_id='list_dag_files',
        bash_command='echo "Files in the DAG directory:" && ls -lh /opt/airflow/dags'
    )
my_task_dag = my_task()