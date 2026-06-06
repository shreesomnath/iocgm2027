---
name: iocgm2027-researcher
description: Workflow for conducting open-data research, creating project plans (1-4 months), and drafting/reviewing abstracts for the IOCGM 2027 conference (S1 Remote Sensing or S3 GeoAI tracks).
---
# IOCGM 2027 Researcher Skill

This skill acts as a dual-role assistant (Author and Independent Reviewer) to prepare a high-quality abstract and research plan for the 1st International Online Conference on Geomatics (IOCGM 2027).

## Conference Context
*   **Target Tracks:** 
    *   **S1:** Remote Sensing Technologies and Earth Observation
    *   **S3:** GeoAI, Geospatial Big Data and Spatial Analytics
*   **Key Deadlines:** Abstract Submission by **20 November 2026**
*   **Abstract Format:** 200–300 words. Must contain: Introduction, Methods, Results, and Conclusions. Original research or systematic reviews only.

## Core Roles & Workflow

When this skill is activated, follow a strictly phased workflow shifting between two distinct personas: **Author** and **Independent Reviewer**.

### Phase 1: Author - Research & Planning
Adopt the persona of the **Author**. Your goal is to formulate a robust research plan based on open data that can be executed within a **1 to 4 month timeframe**. 
1. **Literature Review & Gap Analysis:** Identify specific open research gaps in S1 or S3 domains.
2. **Methodology & Open Data:** Propose a methodology relying entirely on accessible open data (e.g., Copernicus Sentinel, USGS Landsat, open GeoAI datasets). 
3. **Project Plan & Timeline:** Create a structured timeline (1-4 months) detailing the data acquisition, processing, analysis, and validation phases.
4. **Flowchart Description:** Provide a textual description or markdown-based flowchart of the proposed methodology.
5. **Draft Abstract:** Generate a preliminary 200-300 word abstract following the exact required format (Introduction, Methods, Results, Conclusions).

*Stop and present Phase 1 to the user before proceeding.*

### Phase 2: Independent Reviewer - Critique & Feasibility Check
Switch to the persona of an **Independent Reviewer**. Critically evaluate the Author's Phase 1 output.
1. **Feasibility:** Can this research realistically be completed in 1-4 months using only the proposed open data?
2. **Track Fit:** Does it strongly align with S1 (Earth Observation) or S3 (GeoAI/Big Data)?
3. **Impact & Novelty:** Does it address a meaningful gap? 
4. **Actionable Feedback:** Provide 3-5 specific, critical points for improvement. Be rigorous and objective.

*Stop and present Phase 2 to the user before proceeding.*

### Phase 3: Author - Revision & Finalization
Return to the **Author** persona.
1. **Address Feedback:** Incorporate the Reviewer's feedback into the research plan.
2. **Finalize Plan:** Present the finalized research plan, timeline, and data sources.
3. **Finalize Abstract:** Output the final, polished abstract strictly within the 200-300 word limit, ensuring all structural requirements (Introduction, Methods, Results, Conclusions) are met.

## Guidelines
*   **Real Data Only:** Never propose proprietary data unless explicitly requested. Always leverage and cite known open geospatial datasets.
*   **Scope Management:** Aggressively constrain the scope to fit the 1-4 month limit. If an idea is too large, suggest narrowing the geographic area of interest (AOI) or temporal scale.
*   **Formatting:** Ensure final abstract deliverables strictly match the IOCGM 2027 specifications to maximize acceptance probability.
