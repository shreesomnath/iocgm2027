# Dynamic Multi-Sensor GeoAI Framework for Monsoon-Driven Landslide Susceptibility Evolution and Cross-Basin Transferability in Nepal

**Track:** S3 — GeoAI, Geospatial Big Data and Spatial Analytics  
**Target Conference:** IOCGM 2027 | Abstract Deadline: 20 November 2026  
**Study Area:** Arun Basin (Source Domain) → Trishuli Basin (Target Domain), Nepal

---

## Abstract

Landslide susceptibility models in Nepal are predominantly static — trained once on historical inventories and applied without updating as monsoon dynamics evolve. This study proposes a dynamic, multi-sensor GeoAI framework that integrates Sentinel-1 SAR pre/post-monsoon backscatter change, Sentinel-2 monsoon composites, NASADEM-derived topographic indices (TWI, SPI, curvature), and GPM IMERG rainfall extremes to map time-sensitive landslide susceptibility across the Arun Basin (2021–2025). Quantile Mapping (QM) bias correction aligns IMERG estimates with DHM Nepal gauge records to preserve extreme-event rainfall signatures. An XGBoost ensemble model is trained with SHAP-based explainability to identify dominant conditioning and triggering factors per terrain class. A Few-Shot Transfer Learning experiment then tests whether the Arun-trained model, fine-tuned on only 5% of labeled data, achieves competitive accuracy in the morphologically distinct Trishuli Basin — directly addressing the critical challenge of inventory-scarce basins. This framework directly supports Nepal's National Landslide Risk Management Strategy and demonstrates open-data reproducibility for the broader Hindu Kush Himalayan region.

*(~200 words)*

---

## 1. Introduction and Rationale

Nepal's mountainous terrain hosts some of the world's highest landslide densities, with the monsoon season (June–September) triggering over 80% of annual landslide fatalities. The Arun and Trishuli river basins represent contrasting geomorphological regimes — Arun's deeply incised gorges with thin colluvial soils versus Trishuli's more structurally complex mid-hill geology — making them ideal paired study areas for transferability analysis.

Despite substantial advances in Machine Learning-based Landslide Susceptibility Mapping (LSM), three critical gaps persist:

1. **Temporal Rigidity:** Most published models treat susceptibility as static, ignoring the progressive soil saturation, LULC change, and road-network expansion that unfolds across monsoon seasons (2021–2025 captures Nepal's most damaging recent monsoon period, including the catastrophic September 2024 event).

2. **SAR Underutilization:** Sentinel-1 backscatter has rarely been used as a dynamic moisture-state proxy in Nepal LSM. Raw GRD imagery without Radiometric Terrain Flattening (RTF) produces false signals in high-relief terrain, and corrected SAR features have not been incorporated into a transferable susceptibility framework for this region.

3. **Generalization:** Models trained on well-inventoried basins rarely transfer reliably to data-scarce areas without significant re-labeling. Few-Shot domain adaptation offers a practical path forward for operational deployment.

This study addresses all three gaps through an integrated, open-data pipeline deployable entirely in Google Earth Engine and Python.

---

## 2. Literature Review and Research Gaps

### 2.1 Landslide Hazard Context in Nepal

Nepal's September 2024 extreme rainfall event triggered hundreds of catastrophic landslides across central river basins. Lamichhane et al. (2025) provided a preliminary geospatial assessment of these events, documenting over 3,200 landslides in a six-week window — highlighting the critical need for near-real-time susceptibility models that can update with monsoon intensity data. The co-seismic context also remains important: Pyakurel et al. (2024) demonstrated that ML models incorporating peak ground acceleration, fault proximity, and 12 conditioning factors achieved AUC = 0.94 for the post-2015 Gorkha earthquake landslide inventory, establishing a methodological benchmark for Nepal-specific GeoAI work.

**Gap identified:** Both studies treat susceptibility as an event-specific snapshot. No operational framework in the Nepal context updates susceptibility maps continuously as monsoon rainfall accumulates.

### 2.2 Dynamic Landslide Susceptibility Modeling

Lee et al. (2022) demonstrated that integrating rainfall period and accumulated rainfall alongside standard geospatial factors substantially improves temporal LSM accuracy, with XGBoost consistently outperforming SVM and LR models when dynamic triggers are included. Building on this, Ye et al. (2025) specifically evaluated dynamic versus static factor contributions in a Himalayan context, finding that LULC change and seasonal rainfall anomalies together account for 30–40% of susceptibility variation that static models cannot capture.

**Gap identified:** Neither study incorporates Sentinel-1 SAR backscatter change as a soil moisture proxy — a critical pre-failure signal in monsoon-saturated Himalayan soils.

### 2.3 Sentinel-1 SAR for Landslide Applications

Nava et al. (2025) conducted a rigorous multi-sensor evaluation of pre/post-event SAR features in deep learning landslide mapping, showing that multi-temporal Sentinel-1 combinations outperform single-acquisition approaches for identifying post-event debris. The study also confirmed that SAR + optical + DEM fusion produces the highest classification accuracy. Critically, their work used post-event inventory data; pre-event SAR change as a *susceptibility predictor* (rather than a post-event mapper) remains an open methodological direction.

For high-relief Himalayan terrain, Mullissa et al. (2021) established the standard for Sentinel-1 ARD (Analysis Ready Data) preparation in Google Earth Engine, including Radiometric Terrain Flattening (RTF) that eliminates layover and shadow artifacts that would otherwise generate false backscatter anomalies on steep slopes. This correction is essential for SAR-based susceptibility work in the Arun Basin's >45° slope sectors.

**Gap identified:** No Nepal LSM study has applied RTF-corrected Sentinel-1 backscatter change (pre-monsoon to peak-monsoon delta) as a dynamic conditioning factor within an XGBoost framework.

### 2.4 Explainable AI and Physical Consistency

Hussain et al. (2025) applied XGBoost with SHAP to Rudraprayag and Tehri Garhwal (Uttarakhand, India) — a geologically similar Himalayan setting — demonstrating that Distance from Roads, Elevation, Rainfall, and Slope emerge as the dominant SHAP predictors. The study confirmed that XGBoost outperforms RF and SVM when feature importance is validated against physical domain knowledge, providing a model that is both accurate and interpretable by geomorphologists and policymakers. A comparable study specifically integrating SAR-derived moisture change and dynamic rainfall features for Nepal has not been published.

### 2.5 Transfer Learning Across Basins

The challenge of applying models trained on well-inventoried source domains to data-scarce target basins is well-established. Wang et al. (2022) systematically compared domain adaptation (DA) and case-based reasoning (CBR) strategies, finding that combined DA+CBR achieves superior transfer performance over single-strategy methods for landslide susceptibility. More recently, Su et al. (2024) specifically addressed "zero-sample" areas in mountain terrain using feature-space adaptation, achieving competitive AUC even with no target-domain labels. The MDACNN approach of Yu et al. (2025) further extended this to multi-source domain transfer for large-scale, geologically heterogeneous regions.

**Gap identified:** No published transfer learning study targets the Arun-to-Trishuli transition in Nepal, where lithological fingerprints, structural geology, and road-construction intensity differ substantially — making this an important test of generalization limits in the HKH region.

### 2.6 GPM Rainfall Bias Correction for Nepal

Nepal et al. (2021) evaluated IMERG V06 performance across 279 gauge stations in the southern Himalayan slope, finding that IMERG has a systematic underestimation bias (–2.49 mm/day) with reduced skill at capturing extreme daily events (RX1Day, RX5Day). Nair et al. (2025) demonstrated that a novel ensemble bias correction method (EQMX-RF) applied to the Budhi Gandaki River Basin substantially improved IMERG estimates across all quantiles, with particular improvement for extreme events above the 95th percentile. Quantile Mapping specifically has been shown to outperform Linear Scaling for preserving the upper tail of rainfall distributions (Andari et al., 2024) — essential for extreme-event landslide triggering.

**Gap identified:** No Nepal LSM study integrates QM-corrected IMERG as a dynamic rainfall trigger, despite evidence that uncorrected IMERG systematically underestimates the extreme events most responsible for triggering mass movements.

---

## 3. Methodology

### 3.1 Data Sources (All Open Access)

| Feature | Dataset | Resolution | Access |
|---|---|---|---|
| Elevation, slope, aspect, TWI, SPI, curvature | NASADEM (`NASA/NASADEM_HGT/001`) | 30 m | NASA Earthdata (free) |
| Upstream drainage area | MERIT Hydro (`MERIT/Hydro/v1_0_1`) | 90 m | Free (GEE) |
| Spectral indices (NDVI, NDWI, BSI) | Sentinel-2 SR Harmonized (GEE) | 10 m | Copernicus (free) |
| SAR backscatter + dynamic change | Sentinel-1 GRD + RTF (Mullissa 2021) | 10 m | Copernicus (free) |
| Monsoon rainfall (mean + extremes) | GPM IMERG V06 Final (`NASA/GPM_L3/IMERG_V06`) | 0.1° | NASA Earthdata (free) |
| Land cover | ESA WorldCover 2021 (`ESA/WorldCover/v200`) | 10 m | ESA (free) |
| Gauge-based QM calibration | DHM Nepal station records | Point | DHM Nepal (open) |
| Landslide inventory (labels) | NDRRMA 2021 inventory + BiPad 2024 update | Vector | Government of Nepal |

### 3.2 Feature Engineering

**Static topographic features:** Slope, aspect, plan/profile curvature, TWI, SPI, distance to rivers — all derived from NASADEM using GEE `ee.Terrain` and MERIT Hydro upstream area.

**Dynamic Sentinel-1 SAR feature:** Pre-monsoon (Mar–May) to peak-monsoon (Jul–Aug) VV backscatter delta (ΔVV) is computed after RTF correction. This change captures progressive soil moisture increase — a direct proxy for slope instability in unsaturated to near-saturated transition. This is the framework's key novel dynamic feature not present in prior Nepal LSM literature.

**Sentinel-2 monsoon composite:** JJAS (Jun–Sep) median composites across 2021–2025 produce NDVI, NDWI, and BSI. SCL-based cloud masking is applied (replacing less accurate QA60 for SR products).

**Rainfall features:** GPM IMERG annual monsoon totals (JJAS sum) and maximum single-year monsoon accumulation are extracted per pixel. Quantile Mapping bias correction is applied in post-processing against 12 available DHM gauge stations in the Arun watershed.

### 3.3 Model Architecture

**XGBoost Ensemble with SHAP Explainability:**

Following Hussain et al. (2025), an XGBoost model is trained using 18 conditioning factors. Hyperparameter tuning uses Bayesian Optimization (Optuna). SHAP values decompose individual predictions to identify which factors dominate susceptibility in each terrain class (valley floors vs. mid-slopes vs. upper catchments). This serves as a physical consistency check — if SAR ΔVV and extreme rainfall (max_monsoon_rain) do not appear in the top-5 SHAP features for monsoon-triggered landslides, the dynamic feature engineering requires revision.

**Performance Evaluation:**
- AUC-ROC, F1, Kappa coefficient
- Spatial cross-validation using geographic k-fold splits (prevents spatial autocorrelation leakage)
- Separate evaluation on the 2024 extreme-event validation inventory

### 3.4 Few-Shot Transfer Learning

Zero-Shot baseline: Arun-trained XGBoost applied directly to Trishuli without any fine-tuning.

Few-Shot fine-tuning: 5% of Trishuli labeled inventory is used to adapt the model via Feature-Aligned Transfer (feature distribution matching in input space, following Su et al., 2024). The key test is whether 5% of labels recovers AUC performance to within 5% of a fully-supervised Trishuli model.

**Why Arun → Trishuli?** The basins differ in lithological fingerprint (Tibetan Tethyan Sedimentary vs. Higher Himalayan Crystalline sequences), drainage basin geometry, and road construction density — making this a genuine out-of-distribution transfer, not a trivial spatial extension.

---

## 4. Project Timeline (4 Months)

| Month | Tasks | Deliverable |
|---|---|---|
| **Month 1** | GEE feature extraction for both basins; RTF correction using Mullissa et al. module; QM bias correction of IMERG in Python (scipy.stats) using DHM gauge data | Feature stack GeoTIFFs (Arun + Trishuli) |
| **Month 2** | Landslide inventory preparation (NDRRMA + BiPad 2024); XGBoost training + hyperparameter tuning; SHAP analysis | Trained model + SHAP plots |
| **Month 3** | Transfer learning experiments (zero-shot + few-shot); 2024 extreme-event validation; susceptibility map generation | Transfer AUC comparison + susceptibility maps |
| **Month 4** | Manuscript writing; figure finalization; IOCGM abstract preparation | Abstract submitted by 20 Nov 2026 |

---

## 5. Expected Outcomes and Impact

1. **First Nepal LSM study** integrating RTF-corrected Sentinel-1 pre/post-monsoon backscatter change as a dynamic conditioning factor.
2. **SHAP-validated evidence** of the relative contribution of SAR moisture signals vs. topographic vs. rainfall features — directly informative for operational early warning system design under Nepal's NDRRMA.
3. **Transferability benchmark** for the Himalayan Hindu Kush region: establishing how much labeled inventory is needed in a new basin to achieve operational accuracy, directly useful for NDRRMA and ICIMOD planning.
4. **Open, reproducible pipeline** entirely executable in Google Earth Engine + Python, lowering the barrier for adoption by national disaster risk agencies in Nepal and the wider HKH.

---

## 6. References

Hussain, M., Chaudhary, B. S., Ahmad, Z., & Khan, R. A. (2025). Enhancing landslide susceptibility predictions with XGBoost and SHAP: a data-driven explainable AI method. *Geocarto International*, 40(1), Article 2514725. https://doi.org/10.1080/10106049.2025.2514725

Lamichhane, K., Biswakarma, K., Acharya, B., Karki, S., KC, R., Subedi, M., & Sharma, K. (2025). Preliminary assessment of September 2024 extreme rainfall–induced landslides in Central Nepal. *Landslides*, 22, 3281–3295. https://doi.org/10.1007/s10346-025-02450-x

Lee, J.-J., Song, M.-S., Yun, H.-S., & Yum, S.-G. (2022). Dynamic landslide susceptibility analysis that combines rainfall period, accumulated rainfall, and geospatial information. *Scientific Reports*, 12, 18970. https://doi.org/10.1038/s41598-022-21795-z

Mullissa, A., Vollrath, A., Odongo-Braun, C., Slagter, B., Balling, J., Gou, Y., Gorelick, N., & Reiche, J. (2021). Sentinel-1 SAR backscatter analysis ready data preparation in Google Earth Engine. *Remote Sensing*, 13(10), 1954. https://doi.org/10.3390/rs13101954

Nair, A. V., Wi, S., & Kayastha, R. B. (2025). On the challenges of simulating streamflow in glacierized catchments of the Himalayas using satellite and reanalysis forcing data. *Journal of Hydrometeorology*, 25, 847–866. https://doi.org/10.1175/JHM-D-23-0048.1

Nava, L., Mondini, A. C., Barra, A., & Strozzi, T. (2025). Landslide mapping with deep learning: the role of pre-/post-event SAR features and multi-sensor data fusion. *GIScience & Remote Sensing*, 62(1), Article 2502214. https://doi.org/10.1080/15481603.2025.2502214

NDRRMA. (2021). *National Landslide Risk Management Strategy for Nepal*. Government of Nepal, National Disaster Risk Reduction and Management Authority.

Nepal, B., Shrestha, D., Sharma, S., Shrestha, M. S., Aryal, D., & Shrestha, N. (2021). Assessment of GPM-Era satellite products' (IMERG and GSMaP) ability to detect precipitation extremes over mountainous country Nepal. *Atmosphere*, 12(2), 254. https://doi.org/10.3390/atmos12020254

Pyakurel, A., KC, D., & Dahal, B. K. (2024). Enhancing co-seismic landslide susceptibility, building exposure, and risk analysis through machine learning. *Scientific Reports*, 14, 5889. https://doi.org/10.1038/s41598-024-54898-w

Su, Y., Fu, J., Lai, X., Huang, W., & Xie, X. (2024). Feature adaptation for landslide susceptibility assessment in "no sample" areas. *Gondwana Research*, 131, 1–17. https://doi.org/10.1016/j.gr.2023.12.001

Wang, Z., Goetz, J., & Brenning, A. (2022). Transfer learning for landslide susceptibility modeling using domain adaptation and case-based reasoning. *Geoscientific Model Development*, 15(23), 8765–8784. https://doi.org/10.5194/gmd-15-8765-2022

Ye, P., Yu, B., Chen, W., Liu, K., & Ye, T. (2025). Integrating dynamic factors for predicting future landslide susceptibility. *Environmental Earth Sciences*, 84, Article 169. https://doi.org/10.1007/s12665-025-12094-7
