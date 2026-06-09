# Research Plan: Dynamic Multi-Sensor GeoAI Framework for Real-Time Landslide Susceptibility Evolution in Nepal’s Mid-Hills (2021–2026)

## 1. Introduction and Rationale
The Himalayan region, particularly Nepal, is highly vulnerable to rainfall-induced landslides. Traditional Landslide Susceptibility Mapping (LSM) often relies on static topographic factors and provides a "snapshot" of risk. Recent high-impact research (2024-2025) emphasizes the need for **Dynamic LSM** and **Cross-Basin Transferability**, especially using multi-sensor fusion (Sentinel-1 SAR and Sentinel-2 optical). 

This research proposes a robust, open-data GeoAI workflow utilizing an **Ensemble XGBoost** architecture to model the temporal evolution of landslide susceptibility (2021-2026) in the **Arun River Basin** (training) and test its operational transferability in the **Trishuli Basin** (testing). By employing **SHAP (Explainable AI)**, the study will provide physically consistent insights into variable importance across different monsoonal regimes.

## 2. Methodology & Data Sources
### 2.1. Open Data Acquisition
*   **Sentinel-1 (SAR):** C-band GRD (VV/VH polarizations) for soil moisture proxies and surface roughness.
*   **Sentinel-2 (Optical):** High-resolution (10m) multi-spectral imagery for vegetation indices (NDVI, EVI).
*   **ALOS PALSAR / SRTM DEM:** 30m Digital Elevation Model for topographic derivatives (Slope, Aspect, Curvature, TWI).
*   **Rainfall:** CHIRPS daily precipitation data.
*   **Ground Truth Inventories:** NASA Global Landslide Catalog (GLC), Durham/BGS Nepal Inventories, supplemented by manual Google Earth validation.

### 2.2. GeoAI Workflow and Modeling
1.  **Google Earth Engine (GEE) Preprocessing:** Automated cloud masking, radiometric terrain flattening, and generation of multi-temporal feature stacks.
2.  **Ablation Study Design:**
    *   *Model A:* Static Topography Only.
    *   *Model B:* Topography + Optical (Sentinel-2).
    *   *Model C (Synergy):* Topography + Optical + SAR (Sentinel-1/2 fusion).
3.  **Machine Learning Architecture:** XGBoost Classifier optimized via Optuna for hyperparameter tuning.
4.  **Explainability:** Implementation of SHAP values to decode the "black-box" model and quantify the spatial-temporal contribution of each feature.

### 2.3. Cross-Basin Transferability
The model trained in the Arun Basin will be directly applied to the Trishuli Basin to evaluate geographic generalization, a key requirement for national-scale disaster risk reduction strategies.

## 3. Project Timeline (3 Months)

### Month 1: Data Curation & Preprocessing
*   **Week 1-2:** Literature review finalization and study area boundary delineation (QGIS).
*   **Week 3-4:** Develop GEE scripts to extract and download the 2021-2026 feature stack (S1, S2, DEM, Rainfall) for both Arun and Trishuli basins. Prepare the consolidated CSV datasets.

### Month 2: Model Development & Explainability
*   **Week 1-2:** Data cleaning, handling class imbalance (e.g., SMOTE), and initial Logistic Regression baseline modeling in Python.
*   **Week 3-4:** Train Ensemble XGBoost models. Conduct the Ablation Study (Models A, B, C) and generate SHAP summary plots.

### Month 3: Validation, Transferability & Finalization
*   **Week 1-2:** Execute the cross-basin transferability test on the Trishuli dataset. Calculate evaluation metrics (AUC-ROC, F1-Score).
*   **Week 3-4:** Generate final 30m Susceptibility Maps (GeoTIFFs). Draft and finalize the research paper/extended abstract for IOCGM 2027.

## 4. Expected Impact
This study directly addresses gaps identified in the *National Landslide Risk Management Strategy for Nepal* by providing a scalable, dynamic risk assessment tool that leverages open cloud computing, advancing the S3 (GeoAI) track objectives for IOCGM 2027.