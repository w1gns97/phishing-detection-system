import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 데이터 불러오기
df = pd.read_csv("dataset.csv")

# 타겟 컬럼 설정 (필요 시 수정)
target_col = "Result"

X = df.drop(target_col, axis=1)
y = df[target_col]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 모델 학습
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_train, y_train)

# 모델 저장
joblib.dump(model, "rf_model.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")

print("모델 학습 완료 및 저장 완료!")
