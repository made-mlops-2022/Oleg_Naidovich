from unittest import TestCase
from hydra import compose, initialize


# TODO: finish unit tests
class TestPreprocess(TestCase):
    def setUp(self) -> None:
        with initialize(version_base=None, config_path='test_configs'):
            cfg = compose(config_name="test_config")
        self.cfg = cfg

    def test_preprocess(self):
        pass


class TestTrain(TestCase):
    def setUp(self) -> None:
        with initialize(version_base=None, config_path='test_configs'):
            cfg = compose(config_name="test_config")
        self.cfg = cfg

    def test_train(self):
        pass


class TestPredict(TestCase):
    def setUp(self) -> None:
        with initialize(version_base=None, config_path='test_configs'):
            cfg = compose(config_name="test_config")
        self.cfg = cfg

    def test_predict(self):
        pass


class TestUtils(TestCase):
    def setUp(self) -> None:
        with initialize(version_base=None, config_path='test_configs'):
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
