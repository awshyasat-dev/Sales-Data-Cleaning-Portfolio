# Sales Data Cleaning & Preprocessing | Python & Pandas

**Portfolio practice project | Synthetic sales data**

Cleaned and standardized a sample e-commerce sales dataset using Python/Pandas. This is an independently completed practice project, not a paid client engagement.

## At a glance
- **1,000 original records -> 950 cleaned records** (50 exact duplicates removed)
- **55 missing unit prices** filled with the positive-price **median of each product**
- **40 missing quantities** filled with median **3**
- **65 city entries** and **35 order statuses** standardized
- **42 dates** normalized to YYYY-MM-DD across three alternate formats
- **15 negative unit prices (-5)** detected and *retained* as flagged anomalies
- **0 missing cells** and **0 exact duplicate rows** in the cleaned output

## Files
- `original_sales.csv` - original synthetic dataset
- `cleaned_sales.csv` - standardized 8-column CSV (main deliverable)
- `cleaning_report.pdf` - quality checks, findings, caveats, and methodology
- `cleaning_pipeline.py` - **reconstructed** reproducible Python workflow (the actual Jupyter Notebook was not provided)
- `cleaning_audit.csv` - extra imputation flags for audit purposes
- `flagged_unit_prices.csv` - records with nonpositive unit prices needing review

## Important caveat
Imputed prices/quantities are **estimates**, not known transaction values. The 15 records with price -5 were **not fixed**. Do not interpret this output as fully validated accounting or revenue data. Real-client datasets require client approval for financial imputation.

## Reproduce
With Python and Pandas installed, run `python cleaning_pipeline.py` inside this directory. This creates `cleaned_sales.csv`, `cleaning_audit.csv`, and `flagged_unit_prices.csv`.

## Suggested Upwork portfolio description
**Title:** Sales Data Cleaning & Preprocessing with Python and Pandas

Cleaned a 1,000-row synthetic e-commerce dataset by removing 50 exact duplicates, handling 95 missing values with documented median-based imputation, standardizing 65 city labels and 35 order statuses, and normalizing 42 dates. Identified 15 suspicious negative prices and preserved them for review rather than silently changing them. Delivered a cleaned CSV, an audit dataset, and a concise cleaning report.

**My role:** Data cleaning, quality checks, and reporting. **Tools:** Python, Pandas, CSV.
