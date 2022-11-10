from unittest import TestCase
from hydra import compose, initialize


class TestUtils(TestCase):

    def setUp(self) -> None:
        with initialize(version_base=None, config_path='../test_configs'):
            cfg = compose(config_name="test_config")
        self.cfg = cfg

    def test_load_train_test_data(self):
        pass

    def test_save_train_test_data(self):
        pass

    def test_save_model(self):
        pass

    def test_load_model(self):
        pass

    def test_save_scores(self):
        pass

    def test_save_predictions(self):
        pass
