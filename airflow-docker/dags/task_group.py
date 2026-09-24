from airflow.decorators import dag, task
from datetime import datetime
from airflow.utils.task_group import TaskGroup

@dag(
    dag_id="task_group_example",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["task_group", "example"]
)

def task_group_example():
    @task
    def start_task():
        print("Starting the DAG")

    @task
    def task_a():
        print("Task A executed")

    @task
    def task_b():
        print("Task B executed")

    @task
    def task_c():
        print("Task C executed")

    @task
    def end_task():
        print("Ending the DAG")

    start = start_task()

    with TaskGroup("group_1", tooltip="Tasks in Group 1") as group_1:
        a = task_a()
        b = task_b()

    with TaskGroup("group_2", tooltip="Tasks in Group 2") as group_2:
        c = task_c()

    end = end_task()

    start >> group_1 >> group_2 >> end