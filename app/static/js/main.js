
document.addEventListener('DOMContentLoaded', (event) => {
    const analyzeButton = document.getElementById('analyze-button');
    const resultContainer = document.getElementById('result-container');

    analyzeButton.addEventListener('click', () => {
        const pitcherId = document.getElementById('pitcher-id').value;
        const batterId = document.getElementById('batter-id').value;

        fetch(`/analyze?pitcherId=${pitcherId}&batterId=${batterId}`)
            .then(response => response.json())
            .then(data => {
                resultContainer.innerHTML = `
                    <h2>Analysis Result</h2>
                    <p>Pitcher Performance: ${data.pitcherPerformance}</p>
                    <p>Next Pitch Prediction: ${data.nextPitchPrediction}</p>
                    <p>Improvement Suggestions: ${data.improvementSuggestions}</p>
                    <p>Batter Strategy: ${data.batterStrategy}</p>
                `;
            })
            .catch(error => console.error('Error:', error));
    });
});
