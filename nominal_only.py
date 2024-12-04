import pandas as pd

# Load the dataset
file_path = 'numeric_to_nominal_age_dataset.xlsx'
df = pd.read_excel(file_path)

# Identify nominal columns (non-numeric types)
nominal_columns = df.select_dtypes(include=['object']).columns

# Create a new dataset with only nominal columns
nominal_df = df[nominal_columns]

# Save the new dataset
nominal_file_path = 'nominal_only_dataset.xlsx'
nominal_df.to_excel(nominal_file_path, index=False)

print(f"Dataset with only nominal columns saved to {nominal_file_path}")
