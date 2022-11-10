from configs.config import Config
import pandas as pd
import numpy as np
import pickle


def load_train_test_data(cfg: Config):
    X_train = pd.read_csv(cfg.data.path_to_preprocessed_X_train, delimiter=' ').values
    X_test = pd.read_csv(cfg.data.path_to_preprocessed_X_test, delimiter=' ').values
    y_train = pd.read_csv(cfg.data.path_to_preprocessed_y_train, delimiter=' ').values
    y_test = pd.read_csv(cfg.data.path_to_preprocessed_y_test, delimiter=' ').values
    return X_train, X_test, y_train, y_test


def save_train_test_data(cfg: Config, X_train, y_train, X_test, y_test):
    np.savetxt(cfg.data.path_to_preprocessed_X_train, X_train)
    np.savetxt(cfg.data.path_to_preprocessed_y_train, y_train)
    np.savetxt(cfg.data.path_to_preprocessed_X_test, X_test)
    np.savetxt(cfg.data.path_to_preprocessed_y_test, y_test)


def save_model(path_to_model: str, model: object):
    with open(path_to_model, "wb") as file:
        pickle.dump(model, file)


def load_model(path_to_model: str):
    return pickle.load(open(path_to_model, 'rb'))


def save_scores(path_to_metrics: str, scores: dict):
    scores = pd.DataFrame(scores)
    scores.to_csv(path_to_metrics)


def save_predictions(path_to_predictions: str, predictions: np.ndarray):
    np.savetxt(path_to_predictions, predictions)
