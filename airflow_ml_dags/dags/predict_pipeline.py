from pendulum import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from config import DATA_VOLUME_DIR, default_args, FEATURES_TEST, TARGET_TEST, MODEL_DIR


with DAG(
        dag_id="predict_pipeline",
        start_date=datetime(2022, 12, 8, tz="UTC"),
        schedule_interval="@daily",
        default_args=default_args,
        tags=["ml_ops"]
) as dag:
    predict = DockerOperator(
        image="airflow-predict",
        command=f"--features_test_dir {FEATURES_TEST} "
                f"--model_dir {MODEL_DIR}",
        task_id="train",
        network_mode='host',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_VOLUME_DIR, target='/data', type='bind')]
    )

    predict