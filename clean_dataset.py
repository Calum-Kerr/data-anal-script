import pandas as pd

# Load the dataset
file_path = 'coursework2Dataset2024 (1).xlsx'
df = pd.read_excel(file_path)

# Fix 'purpose' column
df['purpose'] = df['purpose'].replace({
    'repars': 'repairs',
    'eduction': 'education',
    'Radio/Tv': 'radio/tv',
    'use car': 'used car'
})

# Fix 'age' column
df['age'] = df['age'].replace({
    0.45: 45,
    0.28: 28,
    1.0: 24,
    222: 22,
    -30: 30,
    333: 33,
    'thirty': 30,
    3.6: 36
})

# Fix 'job' column
df['job'] = df['job'].replace({
    'good': 'skilled',
    'poor': 'unskilled resident'
})

# Fix 'credit_amount' column
credit_amount_corrections = {
    10530000: 1053,
    1237000: 1237,
    3092000: 3092,
    12: 12000,  # new car context
    22: 22000,  # new car context
    1388000: 1388,
    4480000: 448,
    1393000: 1393,
    12: 1200,  # education context
    46790000: 467
}
df['credit_amount'] = df['credit_amount'].replace(credit_amount_corrections)

# Fix 'class' column
df['class'] = df['class'].replace({
    1.0: 'good',
    0.0: 'bad'
})

# Save the cleaned dataset
cleaned_file_path = 'cleaned_dataset.xlsx'
df.to_excel(cleaned_file_path, index=False)

print(f"Dataset cleaned and saved to {cleaned_file_path}")