import joblib
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from feature_extractor import extract_features

# 모델 로드
model = joblib.load("rf_model.pkl")
feature_names = joblib.load("feature_names.pkl")

def plot_feature_importance(input_df):
    importances = model.feature_importances_

    plt.figure(figsize=(8, 4))
    plt.barh(feature_names, importances)
    plt.title("Feature Importance")
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    return base64.b64encode(buffer.getvalue()).decode()

def predict_url(url):
    features = extract_features(url)
    df = pd.DataFrame([features])

    # 누락된 컬럼 보정
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]

    # 예측
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0]

    phishing_prob = round(probability[0] * 100, 2)
    normal_prob = round(probability[1] * 100, 2)

    result = "정상 사이트" if prediction == 1 else "피싱 사이트"

    # 시각화 생성
    feature_plot = plot_feature_importance(df)

    return {
        "result": result,
        "phishing_prob": phishing_prob,
        "normal_prob": normal_prob,
        "feature_plot": feature_plot,
        "features": features
    }
