
import unittest
from services import data_preprocessing

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.preprocessor = data_preprocessing.DataPreprocessor()

    def test_load_data(self):
        data = self.preprocessor.load_data('data/raw/player_data.csv')
        self.assertIsNotNone(data)

    def test_clean_data(self):
        data = self.preprocessor.load_data('data/raw/player_data.csv')
        cleaned_data = self.preprocessor.clean_data(data)
        self.assertIsNotNone(cleaned_data)

    def test_split_data(self):
        data = self.preprocessor.load_data('data/raw/player_data.csv')
        cleaned_data = self.preprocessor.clean_data(data)
        train_data, test_data = self.preprocessor.split_data(cleaned_data)
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(test_data)

if __name__ == '__main__':
    unittest.main()
