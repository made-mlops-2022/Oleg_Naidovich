from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DatasetConfig:
    path_to_raw_data: str
    path_to_preprocessed_X_train: str
    path_to_preprocessed_y_train: str
    path_to_preprocessed_X_test: str
    path_to_preprocessed_y_test: str
    path_to_predictions: str


@dataclass(frozen=True)
class FeaturesConfig:
    cat_features: List[str]
    num_features: List[str]
    target_feature: str


@dataclass(frozen=True)
class ModelConfig:
    clf_name: str
    clf_params: dict
    path_to_model: str
    n_folds: int
    test_size: int
    random_state: int


@dataclass(frozen=True)
class TransformerConfig:
    path_to_transformer: str


@dataclass(frozen=True)
class Config:
    model: ModelConfig
    data: DatasetConfig
    features: FeaturesConfig
    transformer: TransformerConfig
    path_to_report: str
    path_to_metrics: str
