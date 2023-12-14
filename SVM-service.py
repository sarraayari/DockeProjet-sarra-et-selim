from flask import Flask, request, jsonify
import numpy as np
from sklearn.svm import SVC
from joblib import dump, load
import base64
import io
import librosa

app = Flask(__name__)
	
types=["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]
try:
    # Attempt to load the saved model using joblib.load
    model = load("OurModel.pkl")
except FileNotFoundError:
    # If model file is not found, train a new model and save it
    print("Model file not found. Training a new model...")
    # model = SVC()
    # ... Train the model ...
    # dump(model, "model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predicts the musical genre of a wav file.

    Returns:
        The predicted musical genre.
    """
    try:
        # Try to get base64 data from JSON payload
        try:
            base64_data = request.json.get("wav_music", "")
        except Exception:
            return jsonify({"error": "No base64 data provided"})

        if not base64_data:
            return jsonify({"error": "No base64 data provided"})

        # Decode the base64-encoded string to obtain the WAV file content
        wav_data = base64.b64decode(base64_data)

        try:
            # Load audio data using librosa
            audio, sr = librosa.load(io.BytesIO(wav_data), sr=None)
            print(f"Loaded audio with shape: {audio.shape}, sampling rate: {sr}")

            # Compute mel spectrogram
            hop_length = 512
            n_fft = 2048
            n_mels = 128

            S = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
            S_DB = librosa.power_to_db(S, ref=np.max)
            S_DB = S_DB.flatten()[:1200]
	   
            # Print mel spectrogram shape
            print(f"Computed mel spectrogram with shape: {S_DB.shape}")

            # Perform prediction using the loaded model
            prediction = model.predict([S_DB])[0]
            return {"genre": types[prediction]}

        except Exception as e:
            return jsonify({"error": f"Error loading audio data: {str(e)}"})

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port =5000)

