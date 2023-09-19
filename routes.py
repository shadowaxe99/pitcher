
from flask import Flask, render_template, request
from services.model_prediction import predict_pitch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_id = request.form['player_id']
        pitch_data = predict_pitch(player_id)
        return render_template('result.html', pitch_data=pitch_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
