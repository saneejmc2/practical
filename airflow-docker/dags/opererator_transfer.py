#Import essential libraries
from datetime import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.providers.common.io.operators.file_transfer import FileTransferOperator

# Define DAG
@dag(
    dag_id='local_file_transfer_dag',
    start_date=datetime(2026, 9, 13),
    catchup=False,
    tags=['file_transfer_local'],
)
def my_task():
    list_dag_files = BashOperator(
        task_id='list_dag_files',
        bash_command='echo "Files in the DAG directory:" && ls -lh /opt/airflow/dags'
    )
    
    transfer_task = FileTransferOperator(
        task_id='transfer_file',
        src='/opt/airflow/dags/sample_file.txt',  # Source file path
        dst='/opt/airflow/dags/transfer/sample_file.txt'  # Destination file path
    )
    
    list_dag_files >> transfer_task

mytask_dag = my_task()