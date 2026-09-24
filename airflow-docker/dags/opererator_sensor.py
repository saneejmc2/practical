from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.providers.common.io.operators.file_transfer import FileTransferOperator

SOURCE_FILE = "/opt/airflow/dags/sample_file.txt"
TRANSFER_DIR = "/opt/airflow/dags/transfer"
TARGET_FILE = f"{TRANSFER_DIR}/sample_file.txt"


@dag(
    dag_id="check_and_transfer_file_simple",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    tags=["sensor1", "sensor_transfer"],
)
def check_and_transfer_file_simple():

    wait_for_file = FileSensor(
        task_id="wait_for_file",
        filepath=TARGET_FILE,
        poke_interval=30,
        timeout=60 * 10,
        mode="poke",
        soft_fail=True,
    )

    delete_target = BashOperator(
        task_id="delete_target_if_exists",
        bash_command=f'[ -f {TARGET_FILE} ] && rm -f {TARGET_FILE} || echo "No file to delete"',
    )

    list_files = BashOperator(
        task_id="list_files",
        bash_command=f'mkdir -p {TRANSFER_DIR} && ls -la {TRANSFER_DIR}',
    )

    copy_file = FileTransferOperator(
        task_id="copy_file_to_transfer",
        src=SOURCE_FILE,
        dst=TARGET_FILE,
    )

    wait_for_file >> delete_target >> list_files >> copy_file


check_and_transfer_file_simple()