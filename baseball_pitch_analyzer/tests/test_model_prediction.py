
import unittest
from services.model_prediction import ModelPrediction

class TestModelPrediction(unittest.TestCase):

    def setUp(self):
        self.model_prediction = ModelPrediction()

    def test_predict_pitch(self):
        result = self.model_prediction.predict_pitch('pitcher_id', 'batter_id')
        self.assertIsInstance(result, dict)
        self.assertIn('prediction', result)

    def test_get_pitcher_insights(self):
        result = self.model_prediction.get_pitcher_insights('pitcher_id')
        self.assertIsInstance(result, dict)
        self.assertIn('insights', result)

    def test_get_batter_advice(self):
        result = self.model_prediction.get_batter_advice('pitcher_id', 'batter_id')
        self.assertIsInstance(result, dict)
        self.assertIn('advice', result)

if __name__ == '__main__':
    unittest.main()
