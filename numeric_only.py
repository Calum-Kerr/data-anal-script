import pandas as pd

# Load the dataset
file_path = 'fixed_nominal_to_numeric_job_dataset.xlsx'
df = pd.read_excel(file_path)

# Identify numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Create a new dataset with only numeric columns
numeric_df = df[numeric_columns]

# Save the new dataset
numeric_file_path = 'numeric_only_dataset.xlsx'
numeric_df.to_excel(numeric_file_path, index=False)

print(f"Dataset with only numeric columns saved to {numeric_file_path}")
