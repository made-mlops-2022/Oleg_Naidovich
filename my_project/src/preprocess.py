import pandas as pd
import hydra
from hydra.core.config_store import ConfigStore
from data.preprocess_pipeline import run_preprocess_data
from data.utils import save_model, save_train_test_data
from configs.config import Config
import logging


logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
logger = logging.getLogger('preprocess logger')
logger.setLevel(logging.INFO)


cs = ConfigStore.instance()
cs.store(name='dataset_config', node=Config)


@hydra.main(version_base=None, config_path='../configs', config_name='config')
def preprocess(cfg: Config):
    logger.info('Start Preprocess Pipeline')
    logger.info('Loading Data...')
    raw_data = pd.read_csv(cfg.data.path_to_raw_data)

    logger.info('Preprocessing Data...')
    X_train, X_test, y_train, y_test, transformer = \
        run_preprocess_data(raw_data=raw_data,
                            test_size=cfg.model.test_size,
                            random_state=cfg.model.random_state,
                            num_features=cfg.features.num_features,
                            cat_features=cfg.features.cat_features,
                            target_feature=cfg.features.target_feature)

    logger.info('Saving Data...')
    save_model(cfg.transformer.path_to_transformer, transformer)
    save_train_test_data(cfg, X_train, y_train, X_test, y_test)


if __name__ == '__main__':
    preprocess()
