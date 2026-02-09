from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from random import randint
from datetime import datetime, timedelta

def _choose_best_model(ti):
    accuracy = ti.xcom_pull(task_ids=['training_model_A', 'training_model_B', 'training_model_C'])
    best_accuracy = max(accuracy)
    if (best_accuracy > 8):
        return "accurate"
    return "inaccurate"

def _train_model():
    return randint(1, 10)   

with DAG("my_dag", start_date=datetime(2026, 1, 1),
        schedule="@daily",catchup=False ) as dag:
    
    trainig_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=_train_model
    )

    trainig_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=_train_model
    )

    trainig_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=_train_model
    )

    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_choose_best_model
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate model'"
    )
    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate model'"
    )

    [trainig_model_A, trainig_model_B, trainig_model_C] >> choose_best_model >> [accurate, inaccurate]