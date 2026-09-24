# This is a sample TaskFlow API in Airflow.
from datetime import datetime
from airflow.sdk import dag, task

@dag(
    schedule="@daily",
    start_date=datetime(2026, 9, 8),
    catchup=False,
    tags=["demo", "taskflow"]
)
def taskflow_demo():
    @task()
    def extract():
        data = ["apple", "banana", "cherry"]
        return data

    @task()
    def transform(data: list):
        transformed_data = [item.upper() for item in data]
        return transformed_data

    @task()
    def load(data: list):
        for item in data:
            print(f"Loading data: {item}")

    load(transform(extract()))

taskflow_demo()
