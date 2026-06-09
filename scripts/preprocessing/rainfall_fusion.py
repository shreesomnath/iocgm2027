import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def bias_correct_gpm(dhm_df, gpm_df):
    """
    Fuses DHM Station data with GPM Satellite data using a 
    Linear Scaling / Bias Correction approach to fill gaps.
    
    Parameters:
    - dhm_df: CSV with columns [date, station_id, rain_mm] (has gaps)
    - gpm_df: CSV from GEE with [date, lat, lon, gpm_rain_mm]
    """
    # 1. Merge datasets on date/nearest location
    merged = pd.merge(dhm_df, gpm_df, on='date', suffixes=('_dhm', '_gpm'))
    
    # 2. Calculate Bias (Ratio or Difference)
    # Using Linear Regression to find the scaling factor (DHM = alpha * GPM)
    valid_data = merged.dropna(subset=['rain_mm_dhm'])
    model = LinearRegression(fit_intercept=False)
    model.fit(valid_data[['rain_mm_gpm']], valid_data['rain_mm_dhm'])
    alpha = model.coef_[0]
    
    print(f"Calculated Bias Correction Factor (alpha): {alpha:.4f}")
    
    # 3. Fill Gaps
    # If DHM is missing, use alpha * GPM
    merged['fused_rain'] = merged['rain_mm_dhm'].fillna(merged['rain_mm_gpm'] * alpha)
    
    return merged[['date', 'fused_rain']]

# This ensures we have a continuous 2020-2026 dataset even with DHM gaps.
