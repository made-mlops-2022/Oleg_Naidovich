from datetime import datetime
from docker.types import Mount

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from config import RAW_DATA_DIR, DATA_VOLUME_DIR, default_args


with DAG(
    'generate_data',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2022, 12, 8)
) as dag:
    generate = DockerOperator(
        image='airflow-generate-data',
        command=f'--output-dir {RAW_DATA_DIR}',
        network_mode='bridge',
        task_id='docker-airflow-generate-data',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_VOLUME_DIR, target='/data', type='bind')]
    )

    generate
