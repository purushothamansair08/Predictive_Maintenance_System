import joblib
import pandas as pd

# Load saved model
bundle = joblib.load("full_system.pkl")

pipeline = bundle["pipeline"]
features = bundle["features"]


def predict_failure(input_data):

    df = pd.DataFrame([input_data])

    # Clean column names
    df.columns = df.columns.str.replace(
        '[^A-Za-z0-9_]+',
        '_',
        regex=True
    )

    # Encode categorical
    df = pd.get_dummies(df, columns=['Type'])

    # Feature engineering
    df['temp_diff'] = (
        df['Process_temperature_K_']
        - df['Air_temperature_K_']
    )

    df['load_factor'] = (
        df['Torque_Nm_']
        * df['Rotational_speed_rpm_']
    )

    # Align columns
    df = df.reindex(columns=features, fill_value=0)

    # Prediction
    prediction = int(pipeline.predict(df)[0])

    # Probability
    probability = float(
        pipeline.predict_proba(df)[0][1]
    )

    # Health score
    health_score = round(
        100 - (probability * 100),
        2
    )

    # Risk level
    if probability < 0.3:
        risk = "Low"

    elif probability < 0.7:
        risk = "Medium"

    else:
        risk = "High"

    # Recommendation
    if risk == "High":
        recommendation = (
            "Immediate maintenance inspection required"
        )

    elif risk == "Medium":
        recommendation = (
            "Schedule maintenance check soon"
        )

    else:
        recommendation = (
            "Machine operating normally"
        )

    return {
        "prediction": prediction,
        "probability": round(probability * 100, 2),
        "health_score": health_score,
        "risk": risk,
        "recommendation": recommendation
    }