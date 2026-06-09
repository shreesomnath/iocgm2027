# Comprehensive Research Plan: A Dynamic Multi-Sensor GeoAI Framework for Landslide Susceptibility Evolution and Cross-Basin Transferability in Nepal

## 1. Introduction and Problem Statement
Nepal’s mid-hills are among the most landslide-prone regions globally, with over 80% of fatalities occurring during the monsoon season (July–September). Despite the proliferation of Landslide Susceptibility Mapping (LSM) studies, a critical gap persists: **existing models are largely static**, failing to account for the dynamic interplay between pre-monsoon vegetation health, monsoon-driven soil saturation, and post-earthquake landscape destabilization. 

Furthermore, the "black-box" nature of traditional Machine Learning (ML) models limits their operational utility for disaster management agencies. This research proposes a **Dynamic GeoAI Framework** that integrates multi-sensor satellite synergy (Sentinel-1/2) with high-resolution topographic data and a novel **Hybrid Rainfall Fusion** strategy. By employing **Explainable AI (XAI)**, this study aims to transition from simple "where" mapping to a causal "why and when" understanding of landslide triggers in the Arun and Trishuli River Basins.

---

## 2. Literature Review and Research Gaps
### 2.1 State-of-the-Art in Himalayan LSM (2024–2025)
Recent literature (e.g., *Bhattarai et al., 2024*; *Hussain et al., 2025*) has moved toward ensemble deep learning. However, several limitations remain:
*   **The "Static" Limitation:** Most LSMs use a single snapshot of land cover and topography. Studies by *Yu et al. (2025)* suggest that incorporating dynamic soil moisture can improve AUC scores from 0.82 to 0.91, yet this is rarely operationalized in Nepal.
*   **The SAR Challenge:** While Sentinel-1 SAR is theoretically vital for cloud penetration, its implementation in steep Himalayan terrain is hindered by geometric distortions (layover, shadow). Recent breakthroughs in Radiometric Terrain Flattening (RTF) now allow for more reliable backscatter extraction (*Dahal et al., 2025*).
*   **The Transferability Gap:** Models trained in one basin (e.g., East Nepal) often fail in Central Nepal due to "Geological Fingerprinting." Research into Domain Adaptation for LSM is still in its infancy.

### 2.2 Identified Research Gaps to Address:
1.  **Temporal Evolution Gap:** No major study has mapped the continuous evolution of susceptibility in Nepal from 2021 to 2026, a period marked by extreme monsoon anomalies.
2.  **Sensor Synergy Gap:** The specific contribution of Sentinel-1 (SAR) vs. Sentinel-2 (Optical) for *dynamic* susceptibility remains unquantified for the mid-hills.
3.  **Explainability Gap:** There is a lack of physically consistent AI models that align with geomorphological laws (e.g., the relationship between TWI, SAR backscatter, and failure probability).

---

## 3. Methodology
### 3.1 Study Area and Data Fusion
*   **AOI 1 (Arun Basin):** Training site characterized by high relief and intensive infrastructure development.
*   **AOI 2 (Trishuli Basin):** Testing site for spatial transferability, representing Central Nepal's seismic-prone geology.
*   **Hybrid Rainfall Fusion:** We address the "DHM Gap" (2020-2023) by fusing DHM Nepal station data with GPM IMERG V07 using a linear bias correction.
    *   $P_{fused} = w_1 P_{DHM} + w_2 (\alpha P_{GPM})$, where $\alpha$ is the calibration coefficient derived from pre-2020 overlapping data.

### 3.2 Feature Engineering & Model Architecture
*   **Dynamic Features:** Monthly NDVI (Sentinel-2), VV/VH Backscatter (Sentinel-1), and Antecedent Rainfall (GPM/DHM).
*   **Static Features:** Slope, Aspect, TWI, Distance to Road/Fault, Geology (DMG Nepal).
*   **Modeling:** **Ensemble XGBoost** with SHAP-based interpretability.
    *   **Ablation Study:** Comparing Model A (Topo), Model B (Topo+Opt), and Model C (Topo+Opt+SAR).

---

## 4. Implementation Timeline (3 Months)
| Week | Focus Area | Key Deliverable |
| :--- | :--- | :--- |
| **1-2** | **Literature & Data** | Comprehensive review of 10+ core papers; DHM/GPM fusion script. |
| **3-4** | **GEE Extraction** | 2021-2026 Feature Stacks (S1, S2, DEM) exported for both basins. |
| **5-6** | **Model Training** | XGBoost baseline vs. Ensemble; Hyperparameter tuning (Optuna). |
| **7-8** | **Ablation & XAI** | Model C validation; SHAP summary and dependence plots. |
| **9-10**| **Transferability** | Cross-basin testing; Calculation of Transferability Robustness Index. |
| **11-12**| **Finalization** | LaTeX compilation; GitHub repo documentation; IOCGM Abstract. |

---

## 5. Technical Rigor and Expected Impacts
This study will provide:
1.  **A scalable GeoAI pipeline** for NDRRMA (Nepal) to update susceptibility maps near-real-time.
2.  **Scientific insight** into the role of SAR-based moisture proxies in Himalayan slope stability.
3.  **A high-impact publication** addressing the global need for generalizable landslide models.
