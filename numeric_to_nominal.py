import pandas as pd

# Load the dataset
file_path = 'cleaned_dataset.xlsx'
df = pd.read_excel(file_path)

# Specify the column to transform
column_to_transform = 'age'

# Transformation logic: Numeric to Nominal
def numeric_to_nominal(value):
    if value <= 18:
        return 'Teen'
    elif 19 <= value <= 25:
        return 'Young'
    elif 26 <= value <= 40:
        return 'Young Middle'
    elif 41 <= value <= 60:
        return 'Middle'
    elif 61 <= value <= 75:
        return 'Senior'
    else:
        return 'Old'

df[column_to_transform] = df[column_to_transform].apply(numeric_to_nominal)

# Save the transformed dataset
transformed_file_path = 'numeric_to_nominal_age_dataset.xlsx'
df.to_excel(transformed_file_path, index=False)

print(f"Numeric to Nominal transformation for '{column_to_transform}' completed. File saved to {transformed_file_path}")