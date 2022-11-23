import hydra
from hydra.core.config_store import ConfigStore
from configs.config import Config
from models.predict_pipeline import run_predict_pipeline
from data.utils import load_train_test_data, save_predictions, load_model
import logging


logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
logger = logging.getLogger('preprocess logger')
logger.setLevel(logging.INFO)


cs = ConfigStore.instance()
cs.store(name='dataset_config', node=Config)


@hydra.main(version_base=None, config_path='../configs', config_name='config')
def predict(cfg: Config):
    logger.info('Start Predict Pipeline')
    logger.info('Loading Data...')
    X_train, X_test, y_train, y_test = load_train_test_data(cfg)
    clf = load_model(cfg.model.path_to_model)

    logger.info('Predicting...')
    predictions = run_predict_pipeline(X_test, y_test, clf)

    logger.info('Saving predicitons...')
    save_predictions(cfg.data.path_to_predictions, predictions)


if __name__ == '__main__':
    predict()
