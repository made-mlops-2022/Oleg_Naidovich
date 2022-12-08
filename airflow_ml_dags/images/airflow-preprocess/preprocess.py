import os
from os.path import join
import shutil

import click
import pandas as pd
from sklearn.impute import SimpleImputer


@click.command('preprocess')
@click.option('--features_raw_dir', type=click.Path(), help='Path to raw data')
@click.option('--features_preprocessed_dir', type=click.Path(), help='Path to processed data')
def preprocess_data(features_raw_dir: str, features_preprocessed_dir: str):
    os.makedirs(features_preprocessed_dir, exist_ok=True)
    data = pd.read_csv(join(features_raw_dir, 'data.csv'))

    imp = SimpleImputer(strategy='most_frequent')
    X_precessed = imp.fit_transform(data)

    processed_data = pd.DataFrame(X_precessed, columns=data.columns)
    processed_data.to_csv(join(features_preprocessed_dir, 'data.csv'), index=False)

    shutil.copyfile(join(features_raw_dir, 'target.csv'), join(features_preprocessed_dir, 'target.csv'))


if __name__ == '__main__':
    preprocess_data()
