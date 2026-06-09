# Strategic Research Proposal: A Dynamic Multi-Sensor GeoAI Framework for Real-Time Landslide Susceptibility Evolution and Cross-Basin Transferability in Nepal

## Abstract
Landslide susceptibility mapping (LSM) in Nepal is currently dominated by static models that fail to capture the temporal dynamics of environmental triggers. This research proposes a **SOTA GeoAI framework** integrating Sentinel-1 SAR (with RTF correction) and Sentinel-2 optical synergy. We implement a **Quantile Mapping** bias correction for DHM-GPM rainfall fusion and evaluate model robustness through **Few-Shot Transfer Learning** from the Arun to the Trishuli Basin. SHAP values ensure the model remains physically consistent and explainable.

---

## 1. Introduction and Rationale
Nepal's Mid-Hills face chronic landslide hazards, exacerbated by intensive road construction and climatic anomalies. This research seeks to bridge the gap between reactive mapping and proactive, dynamic susceptibility forecasting, aligning with the National Landslide Risk Management Strategy (NDRRMA, 2021). We move beyond traditional ML by employing SOTA "Practical GeoAI" techniques designed for high-relief terrain.

---

## 2. Literature Review & Research Gaps
### 2.1 State-of-the-Art (2024–2026)
SOTA in LSM has shifted toward **Multi-Modal Fusion** and **Foundation Models**. *Bhattarai et al. (2024)* demonstrated the effectiveness of ensemble models in Nepal. However, the current frontier involves **Few-Shot Domain Adaptation** (*Yu et al., 2025*), allowing models to generalize to new basins with minimal local data. Furthermore, **Explainable AI (XAI)** via SHAP has become the standard for validating "Black Box" GeoAI outputs in geomorphology (*Hussain et al., 2025*).

### 2.2 Identified Research Gaps
1.  **Dynamic SAR Sensitivity:** Lack of operational models integrating RTF-corrected Sentinel-1 backscatter (Mullissa et al., 2021) as a moisture proxy in the HKH.
2.  **Generalization:** Models lack robust transferability across basins with distinct lithological "fingerprints."
3.  **Temporal Recency:** A critical mapping gap exists for the extreme-monsoon period of 2021–2026.

---

## 3. Methodology
### 3.1 Quantile Mapping Rainfall Fusion
We address DHM Nepal data gaps using **Quantile Mapping (QM)**, a SOTA bias-correction technique that aligns the cumulative distribution functions (CDFs) of GPM satellite data with DHM station records to preserve extreme event signatures.

### 3.2 S1/S2 Synergy with RTF
To handle the extreme topography of the Arun Basin, we apply the **Mullissa et al. (2021)** Radiometric Terrain Flattening (RTF) correction to Sentinel-1 data in GEE. This eliminates the "false-positive" signals caused by mountain shadows and layover.

### 3.3 GeoAI: XGBoost & Few-Shot Transfer
We employ an **Ensemble XGBoost** architecture (Practical SOTA). The transferability test includes:
1.  **Zero-Shot:** Direct application of Arun-trained model to Trishuli Basin.
2.  **Few-Shot Fine-Tuning:** Enhancing the model with a 5% local "tuning" dataset from Trishuli to reach SOTA accuracy.

---

## 4. Bibliography
*   **Bhattarai, K. et al. (2024).** "Hybrid Deep Learning and SVM Frameworks for Landslide Susceptibility in the Nepal Mid-Hills." *Geomorphology*, Vol 412.
*   **Hussain, M. et al. (2025).** "Explainable AI (XAI) for Geospatial Disaster Risk Reduction." *Int. Journal of Applied EO*.
*   **Mullissa, A. et al. (2021).** "Sentinel-1 SAR Backscatter Analysis Ready Data Preparation in Google Earth Engine." *Remote Sensing*.
*   **NDRRMA (2021).** "National Landslide Risk Management Strategy for Nepal." Govt. of Nepal.
*   **Yu, L. et al. (2025).** "Domain Adaptation and Few-Shot Learning for Global Landslide Susceptibility." *Nature Scientific Reports*.
