import hydra
from hydra.core.config_store import ConfigStore
from models import run_train_pipeline
from data.utils import load_train_test_data, save_model, save_scores
from configs.config import Config
import logging


logging.basicConfig(format="%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
logger = logging.getLogger('train logger')
logger.setLevel(logging.INFO)


cs = ConfigStore.instance()
cs.store(name='train', node=Config)


@hydra.main(version_base=None, config_path='../configs', config_name='config')
def train(cfg: Config):
    logger.info('Start Train Pipeline')
    logger.info('Loading Data...')

    X_train, X_test, y_train, y_test = load_train_test_data(cfg)
    clf_name, clf_params = cfg.model.clf_name, cfg.model.clf_params
    n_folds = cfg.model.n_folds

    logger.info('Training model...')
    clf, scores = run_train_pipeline(X_train, y_train.ravel(),
                                     clf_name, clf_params, n_folds)

    logger.info('Saving model and metrics...')
    save_scores(cfg.path_to_metrics, scores)
    save_model(path_to_model=cfg.model.path_to_model, model=clf)


if __name__ == '__main__':
    train()
