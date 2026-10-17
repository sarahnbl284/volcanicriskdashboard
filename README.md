# volcanicriskdashboard
Analisis Statistik &amp; Pemodelan Risiko Erupsi Gunung Berapi untuk Estimasi Potensi Kerugian Berbasis Data Historis

# A data analytics project exploring historical volcanic eruption records to understand eruption frequency, Volcanic Explosivity Index (VEI), and recorded economic damage. The project presents the findings in an Web Streamlit.
Scope note: This dashboard summarizes historical records and observed patterns. It is an exploratory risk-analysis project, not a causal model and not a forecast of future eruptions or losses.

# Project Overview
Volcanic eruptions can differ in frequency and intensity, and their recorded impacts can vary across locations. This project analyzes historical eruption data to answer three main questions:
1. How are recorded eruptions distributed by VEI?
2. How does recorded economic-damage severity vary across VEI levels?
3. Which countries have the largest cumulative recorded economic losses in the dataset?
The analysis began with 877 records. After data preparation, 876 events were analyzed. Data availability varies by question: 701 records had a VEI value, 215 had both VEI and an economic-damage category, and only 20 had both VEI and an actual-loss value.

# Dashboard
Open the interactive Streamlit Dashboard using Python
The dashboard contains three pages and includes the following views:
- Eruption Trend — historical eruption trends over time.
- VEI Distribution — frequency of events by VEI.
- VEI × Economic Damage — relationship between VEI groups and recorded damage categories.
- Historical Country Loss — cumulative recorded economic loss by country.
- Country × VEI — comparison of recorded eruption intensity across countries.
- Eruption Location Map — geographic view of eruption records.

# Key Findings
- VEI 2 and VEI 3 were the most frequent categories in the records with VEI data: 237 and 218 events respectively. Together, they accounted for approximately 64.9% of the 701 records with a VEI value.
- The proportion of records classified as Severe or Extreme economic damage generally tended to increase at higher VEI levels. This is an observed pattern in the available data, not proof that VEI alone caused the damage.
- The United States had the largest cumulative historical losses in this dataset, followed by Indonesia; Spain was also among the top three.
- The dataset spans historical records from 4360 BCE to 2021 CE. Very old records and missing values should be interpreted carefully.

# Data and Limitations
- Dataset filename referenced in the project: volcano-events.csv
- Initial record count: 877
- Events analyzed after preparation: 876
- Records with VEI: 701
- Records with VEI and economic-damage category: 215
- Records with VEI and actual loss: 20
Important limitations:
- Economic-loss figures are available for only a small subset of records; country totals represent recorded values in this dataset, not necessarily the full historical impact.
- The number of observations differs across charts because some fields are missing.
- VEI 0 and VEI 5–7 groups have relatively small sample sizes in the available damage-category data, so their percentages can be sensitive to individual records.
- Historical reporting, data coverage, and currency/value comparability may vary.
- The analysis does not include all factors that influence disaster losses, such as population exposure, infrastructure, asset values, preparedness, or evacuation capacity.
- The dashboard does not establish causation or provide a validated prediction of future losses.

# Tools
- Python and Streamlit — a prototype interface was also developed with country/year filters, a filtered data table, KPI summaries, and trend/distribution charts.
- CSV — tabular event data (volcano-events.csv).
The precise Python package versions and full dependency list were not specified in the project report.

# Suggested Repository Structure
```text
volcanic-eruption-risk-dashboard/
├── README.md
├── volcanic_eruption_clean.csv       # Add only if you are allowed to publish the dataset
├── app.py                  # If the Streamlit prototype source is part of this repository
```

# Project Team
- Nakia Aura Suryanto
- Salma Maulidina
- Sarah Nabila Azzahra
(Data Analyst's Team - PT Vinix7 Aurum September 2026)
