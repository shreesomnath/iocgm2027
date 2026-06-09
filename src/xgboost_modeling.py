import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score, classification_report
from imblearn.over_sampling import SMOTE
import shap
import matplotlib.pyplot as plt

def load_and_prep_data(filepath):
    """Loads CSV exported from GEE and prepares for modeling."""
    df = pd.read_csv(filepath)
    # Assume target column 'is_landslide' exists (1 for landslide, 0 for non-landslide)
    X = df[['elevation', 'slope', 'aspect', 'NDVI', 'VV', 'VH', 'mean_precip']]
    y = df['is_landslide']
    return X, y

def train_ablation_models(X, y):
    """Trains Models A, B, and C for the ablation study."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Handle Class Imbalance
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    
    # Define Feature Sets
    features_A = ['elevation', 'slope', 'aspect', 'mean_precip'] # Topo + Rain
    features_B = features_A + ['NDVI']                           # + Optical
    features_C = features_B + ['VV', 'VH']                       # + SAR (Synergy)
    
    models = {}
    for name, features in zip(['Model A', 'Model B', 'Model C'], [features_A, features_B, features_C]):
        print(f"--- Training {name} ---")
        clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
        clf.fit(X_train_res[features], y_train_res)
        
        preds = clf.predict(X_test[features])
        probs = clf.predict_proba(X_test[features])[:, 1]
        
        auc = roc_auc_score(y_test, probs)
        f1 = f1_score(y_test, preds)
        print(f"AUC-ROC: {auc:.4f} | F1-Score: {f1:.4f}")
        models[name] = clf
        
    return models['Model C'], X_test[features_C]

def run_shap_analysis(model, X_test):
    """Generates SHAP summary plot for Model C."""
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig("shap_summary.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Placeholder for actual data execution
    # X, y = load_and_prep_data('data/arun_basin_samples.csv')
    # best_model, X_test_c = train_ablation_models(X, y)
    # run_shap_analysis(best_model, X_test_c)
    print("XGBoost and SHAP modeling framework initialized.")