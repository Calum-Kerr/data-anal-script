import pandas as pd

# Load the dataset
file_path = 'cleaned_dataset.xlsx'
df = pd.read_excel(file_path)

# Specify the column to transform
column_to_transform = 'job'

# Ensure consistent formatting of strings
df[column_to_transform] = df[column_to_transform].str.strip()

# Transformation logic: Nominal to Numeric
nominal_to_numeric = {
    'skilled': 0,
    "'unskilled resident'": 1,
    "unskilled resident": 1,
    "'high qualif/self emp/mgmt'": 2,
    "'unemp/unskilled non res'": 3
}

# Apply the mapping
df[column_to_transform] = df[column_to_transform].replace(nominal_to_numeric)

# Check for unmatched values
unmapped_values = df[~df[column_to_transform].isin(nominal_to_numeric.values())]

if not unmapped_values.empty:
    print("Unmapped job values detected:", unmapped_values[column_to_transform].unique())

# Save the transformed dataset
transformed_file_path = 'fixed_nominal_to_numeric_job_dataset.xlsx'
df.to_excel(transformed_file_path, index=False)

print(f"Fixed Nominal to Numeric transformation for '{column_to_transform}' completed. File saved to {transformed_file_path}")