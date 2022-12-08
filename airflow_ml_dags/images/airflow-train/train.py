import os
import pickle
import pandas as pd
import click
from sklearn.ensemble import RandomForestClassifier


@click.command()
@click.option("--features_train_dir", required=True)
@click.option("--target_train_dir", required=True)
@click.option("--model_dir", required=True)
def main(features_train_dir: str,
         target_train_dir: str,
         model_dir) -> None:

    X = pd.read_csv(features_train_dir)
    y = pd.read_csv(target_train_dir)

    clf = RandomForestClassifier()
    clf.fit(X, y)

    os.makedirs(model_dir, exist_ok=True)
    with open(model_dir, 'wb+') as file:
        pickle.dump(clf, file)


if __name__ == '__main__':
    main()
