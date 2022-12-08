import os
from os.path import join
import click
import pandas as pd

from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.lib.utils import display_bayesian_network


@click.command('generate')
@click.option('--output-dir', type=click.Path(), help='Path to store train data')
def generate_data(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    synthetic_data = join(output_dir, 'synthetic_data.csv')
    generate_synthetic_data(synthetic_data)

    data = pd.read_csv(synthetic_data)
    target_column = data.columns[-1]
    X, y = data.drop(target_column, axis=1), data[target_column]

    X.to_csv(join(output_dir, 'data.csv'), index=False)
    y.to_csv(join(output_dir, 'target.csv'), index=False)


def generate_synthetic_data(synthetic_data: str):
    input_data = 'synthetic_data.csv'
    description_file = 'description.json'

    features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'ca', 'thal']
    categorical_attributes = {feature: True for feature in features}

    threshold_value = 5
    epsilon = 1
    degree_of_bayesian_network = 2
    num_tuples_to_generate = 100

    describer = DataDescriber(category_threshold=threshold_value)
    describer.describe_dataset_in_correlated_attribute_mode(dataset_file=input_data,
                                                            epsilon=epsilon,
                                                            k=degree_of_bayesian_network,
                                                            attribute_to_is_categorical=categorical_attributes)
    describer.save_dataset_description_to_file(description_file)
    display_bayesian_network(describer.bayesian_network)
    generator = DataGenerator()
    generator.generate_dataset_in_correlated_attribute_mode(num_tuples_to_generate, description_file)
    generator.save_synthetic_data(synthetic_data)
    os.remove(description_file)


if __name__ == '__main__':
    generate_data()
