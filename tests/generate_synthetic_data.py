from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.lib.utils import display_bayesian_network


def generate_synthetic_data():
    input_data = '../my_project/data/raw/heart_cleveland.csv'
    description_file = 'synthetic_data/description.json'
    synthetic_data = 'synthetic_data/heart_cleveland.csv'

    threshold_value = 5
    categorical_attributes = dict.fromkeys(['sex', 'cp', 'fbs', 'restecg', 'exang', 'ca', 'thal'], True)
    epsilon = 1
    degree_of_bayesian_network = 2
    num_tuples_to_generate = 200

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


if __name__ == '__main__':
    generate_synthetic_data()
