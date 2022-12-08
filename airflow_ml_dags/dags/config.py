from datetime import timedelta
from airflow.models import Variable


RAW_DATA_DIR = '/data/raw/{{ ds }}'
PROCESSED_DATA_DIR = 'data/precessed/{{ ds }}'

FEATURES_TRAIN = "/data/train_test/{{ ds }}/features_train.csv"
FEATURES_TEST = "/data/train_test/{{ ds }}/features_test.csv"
TARGET_TRAIN = "/data/train_test/{{ ds }}/target_train.csv"
TARGET_TEST = "/data/train_test/{{ ds }}/target_test.csv"

DATA_VOLUME_DIR = Variable.get('data_volume_dir')

MODEL_DIR = "/data/models/{{ ds }}/model.pkl"

default_args = {
    "owner": "oleg-nai",
    "retries": 1,
    "retry_delay": timedelta(seconds=30),
}