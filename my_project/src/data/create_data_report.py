import hydra
from hydra.core.config_store import ConfigStore
import pandas as pd
from dataprep.eda import create_report
from configs.config import Config


cs = ConfigStore.instance()
cs.store(name='dataset_config', node=Config)


@hydra.main(version_base=None, config_path='../../configs', config_name='config')
def create_data_report(cfg: Config):
    raw_data = pd.read_csv(cfg.data.path_to_raw_data_report)
    report = create_report(raw_data)
    report.save(cfg.path_to_report)


if __name__ == '__main__':
    create_data_report()
