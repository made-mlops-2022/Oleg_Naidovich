import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from .create_transformer import create_transformer
from typing import List, Tuple


def run_preprocess_data(raw_data: pd.DataFrame,
                        test_size: int,
                        random_state: int,
                        num_features: List[str],
                        cat_features: List[str],
                        target_feature: str):
    X_train, X_test, y_train, y_test = split_train_test_data(X=raw_data.drop(columns=target_feature),
                                                             y=raw_data[target_feature],
                                                             test_size=test_size,
                                                             random_state=random_state)

    transformer = create_transformer(cat_features=cat_features,
                                     num_features=num_features)
    X_train = transformer.fit_transform(X_train)
    X_test = transformer.transform(X_test)

    return X_train, X_test, y_train, y_test, transformer


def split_train_test_data(X: pd.DataFrame, y: pd.DataFrame,
                          test_size: str,
                          random_state: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
