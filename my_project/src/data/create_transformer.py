from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from typing import List


def create_cat_pipeline() -> Pipeline:
    return Pipeline([('impute', SimpleImputer(strategy='most_frequent')),
                     ('ohe', OneHotEncoder())])


def create_num_pipeline() -> Pipeline:
    return Pipeline([('impute', SimpleImputer(strategy='mean')),
                     ('scaler', StandardScaler())])


def create_transformer(cat_features: List[str], num_features: List[str]) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [('cat_pipeline', create_cat_pipeline(), list(cat_features)),
         ('num_pipeline', create_num_pipeline(), list(num_features))])
    return transformer
