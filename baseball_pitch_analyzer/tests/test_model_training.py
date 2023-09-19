
import unittest
from baseball_pitch_analyzer.services import model_training
from tensorflow.keras.models import Sequential

class TestModelTraining(unittest.TestCase):

    def setUp(self):
        self.model_training = model_training.ModelTraining()

    def test_train_pitch_prediction_model(self):
        model = self.model_training.train_pitch_prediction_model()
        self.assertIsInstance(model, Sequential)

    def test_train_performance_analysis_model(self):
        model = self.model_training.train_performance_analysis_model()
        self.assertIsInstance(model, Sequential)

if __name__ == '__main__':
    unittest.main()
