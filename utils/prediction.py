import joblib
import pandas as pd

from tensorflow.keras.models import load_model

from utils.constants import THRESHOLD

MODEL = load_model("models/cardio_dnn.keras")
SCALER = joblib.load("models/cardio_scaler.pkl")


def predict(features_df):

    scaled = SCALER.transform(features_df)

    probability = MODEL.predict(
        scaled,
        verbose=0
    )[0][0]

    prediction = int(probability >= THRESHOLD)

    return prediction, probability