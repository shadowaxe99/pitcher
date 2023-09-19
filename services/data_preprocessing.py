
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_data():
    player_data = pd.read_csv('../data/raw/player_data.csv')
    pitch_data = pd.read_csv('../data/raw/pitch_data.csv')
    return player_data, pitch_data

def preprocess_data(player_data, pitch_data):
    # Merge player and pitch data
    data = pd.merge(player_data, pitch_data, on='player_id')

    # Drop unnecessary columns
    data.drop(['player_id', 'game_id'], axis=1, inplace=True)

    # Handle categorical data
    categorical_cols = ['pitch_type', 'batter_stance', 'pitcher_throws']
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

    # Normalize numerical data
    numerical_cols = ['pitch_speed', 'pitch_angle', 'batter_avg']
    scaler = MinMaxScaler()
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

    return data, label_encoders, scaler

if __name__ == "__main__":
    player_data, pitch_data = load_data()
    data, label_encoders, scaler = preprocess_data(player_data, pitch_data)
    data.to_csv('../data/processed/data.csv', index=False)
