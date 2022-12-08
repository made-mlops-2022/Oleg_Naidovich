from pendulum import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, DATA_VOLUME_DIR, default_args, \
    FEATURES_TRAIN, FEATURES_TEST, TARGET_TRAIN, TARGET_TEST, MODEL_DIR


with DAG(
        dag_id="main_pipeline",
        start_date=datetime(2022, 12, 8, tz="UTC"),
        schedule_interval="@weekly",
        default_args=default_args,
        tags=["ml_ops"]
) as dag:
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command=f"--features_raw_dir {RAW_DATA_DIR} "
                f"--features_preprocessed_dir {PROCESSED_DATA_DIR}",
        task_id="preprocess",
        network_mode='host',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_VOLUME_DIR, target='/data', type='bind')]
    )

    train_test_split = DockerOperator(
        image="airflow-train-test-split",
        command=f"--raw_data_dir {RAW_DATA_DIR} "
                f"--features_preprocessed_dir {PROCESSED_DATA_DIR} "
                f"--features_train_dir {FEATURES_TRAIN} "
                f"--features_test_dir {FEATURES_TEST} "
                f"--target_train_dir {TARGET_TRAIN} "
                f"--target_test_dir {TARGET_TEST} ",
        task_id="split",
        network_mode='host',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_VOLUME_DIR, target='/data', type='bind')]
    )

    train = DockerOperator(
        image="airflow-train",
        command=f"--features_train_dir {FEATURES_TRAIN} "
                f"--target_train_dir {TARGET_TRAIN} "
                f"--model_dir {MODEL_DIR}",
        task_id="train",
        network_mode='host',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=DATA_VOLUME_DIR, target='/data', type='bind')]
    )

    preprocess >> train_test_split >> train
