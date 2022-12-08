from datetime import timedelta
from airflow.models import Variable


DATA_DIR = Variable.get('local_data_dir')
default_args = {
    "owner": "oleg-nai",
    "retries": 1,
    "retry_delay": timedelta(seconds=30),
}