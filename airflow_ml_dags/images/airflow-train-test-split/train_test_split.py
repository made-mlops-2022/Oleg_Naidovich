import os
import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.option("--raw_data_dir", required=True)
@click.option("--features_preprocessed_dir", required=True)
@click.option("--features_train_dir", required=True)
@click.option("--features_test_dir", required=True)
@click.option("--target_train_dir", required=True)
@click.option("--target_test_dir", required=True)
def main(raw_data_dir: str,
         features_preprocessed_dir: str,
         features_train_dir: str,
         features_test_dir: str,
         target_train_dir: str,
         target_test_dir: str) -> None:

    features = pd.read_csv(raw_data_dir)
    target = pd.read_csv(features_preprocessed_dir)

    X_train, X_test, y_train, y_test = train_test_split(features, target)

    os.makedirs(os.path.dirname(features_train_dir), exist_ok=True)

    X_train.to_csv(features_train_dir)
    X_test.to_csv(features_test_dir)
    y_train.to_csv(target_train_dir)
    y_test.to_csv(target_test_dir)


if __name__ == '__main__':
    main()
