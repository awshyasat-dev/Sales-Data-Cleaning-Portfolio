import pandas as pd

input_file = "original_sales.csv"
df = pd.read_csv(input_file)

# Remove exact duplicate records
original_rows = len(df)
df = df.drop_duplicates()
duplicates_removed = original_rows - len(df)

# Imputation is illustrative and creates estimates, not confirmed transaction data.
# Only valid positive prices contribute to the per-product median.
price_medians = df[df["Unit_Price"] > 0].groupby("Product")["Unit_Price"].median()

df["Unit_Price_Imputed"] = df["Unit_Price"].isna()  # audit flag
price_missing = int(df["Unit_Price_Imputed"].sum())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Product"].map(price_medians))

qty_missing = df["Quantity"].isna().sum()
qty_median = df["Quantity"].median()
df["Quantity_Imputed"] = df["Quantity"].isna()  # audit flag
df["Quantity"] = df["Quantity"].fillna(qty_median)

# Standardize city names and statuses
for column in ["City", "Status"]:
    df[column] = df[column].str.strip().str.title()

# Parse documented original formats without ambiguous auto-detection
raw = df["Order_Date"]
dates = pd.to_datetime(raw, format="%Y-%m-%d", errors="coerce")
formats = {
    "2026/04/20":"%Y/%m/%d",
    "15-05-2026":"%d-%m-%Y",
    "03/15/2026":"%m/%d/%Y"
}

for value, fmt in formats.items():
    mask = raw.eq(value)
    dates.loc[mask] = pd.to_datetime(raw.loc[mask], format=fmt)

if dates.isna().any():
    raise ValueError("Some dates could not be parsed")

df["Order_Date"] = dates.dt.strftime("%Y-%m-%d")

# Flag anomalies, do not silently alter negative unit prices
flags = df[df["Unit_Price"] <= 0]
flags.to_csv("flagged_unit_prices.csv", index=False)

# Client-facing cleaned CSV retains the original 8-column schema.
df.drop(columns=["Unit_Price_Imputed", "Quantity_Imputed"]).to_csv("cleaned_sales.csv",index=False,float_format="%.2f")

# Internal audit flags to distinguish known vs estimated values
df.to_csv("cleaning_audit.csv",index=False,float_format="%.2f")

print({"duplicates_removed":duplicates_removed, "prices_imputed":price_missing,
       "quantities_imputed":qty_missing,"negative_prices_flagged":len(flags)})
