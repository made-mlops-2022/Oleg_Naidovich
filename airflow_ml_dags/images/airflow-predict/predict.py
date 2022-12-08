import pickle
import pandas as pd
import click


@click.command()
@click.option("--features_test_dir", required=True)
@click.option("--model_dir", required=True)
def main(features_test_dir: str,
         model_dir) -> None:

    X = pd.read_csv(features_test_dir)

    with open(model_dir, 'rb') as file:
        clf = pickle.load(file)

    y_pred = pd.DataFrame(clf.predict(X))
    y_pred.to_csv(model_dir)


if __name__ == '__main__':
    main()
